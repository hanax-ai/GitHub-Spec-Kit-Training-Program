#!/usr/bin/env python3
"""
CodeRabbit Nitpick Comments Analysis Script
Analyzes CodeRabbit review data to identify missed nitpick comments
"""

import json
import re
from datetime import datetime

def load_coderabbit_reviews():
    """Load CodeRabbit review data from JSON file"""
    with open('/home/ubuntu/.external_service_outputs/coderabbit_reviews.json', 'r') as f:
        return json.load(f)

def load_existing_defect_log():
    """Load existing defect log to check what's already been addressed"""
    existing_defects = set()
    try:
        with open('DEFECT_LOG.md', 'r') as f:
            content = f.read()
            # Extract defect IDs
            defect_matches = re.findall(r'DEF-(\d+)', content)
            existing_defects = set(f"DEF-{num}" for num in defect_matches)
    except FileNotFoundError:
        pass
    return existing_defects

def extract_nitpick_comments(reviews):
    """Extract nitpick comments from CodeRabbit reviews"""
    nitpick_comments = []
    
    for review in reviews:
        if review.get('user', {}).get('login') == 'coderabbitai[bot]':
            body = review.get('body', '')
            
            # Look for nitpick section
            if '🧹 Nitpick comments' in body:
                # Extract the nitpick section
                start_marker = '🧹 Nitpick comments'
                end_marker = '</blockquote></details>'
                
                start_idx = body.find(start_marker)
                if start_idx != -1:
                    # Find the end of the nitpick section
                    section_start = body.find('<blockquote>', start_idx)
                    if section_start != -1:
                        # Count blockquote levels to find the matching end
                        section_content = body[section_start:]
                        blockquote_count = 0
                        end_idx = section_start
                        
                        i = 0
                        while i < len(section_content):
                            if section_content[i:i+12] == '<blockquote>':
                                blockquote_count += 1
                                i += 12
                            elif section_content[i:i+13] == '</blockquote>':
                                blockquote_count -= 1
                                if blockquote_count == 0:
                                    end_idx = section_start + i + 13
                                    break
                                i += 13
                            else:
                                i += 1
                        
                        nitpick_section = body[start_idx:end_idx]
                        
                        # Parse individual nitpick comments
                        file_sections = re.findall(r'<summary>([^<]+)</summary><blockquote>(.*?)</blockquote></details>', nitpick_section, re.DOTALL)
                        
                        for file_name, file_content in file_sections:
                            # Extract individual comments within each file
                            comment_matches = re.findall(r'`([^`]+)`: \*\*(.*?)\*\*(.*?)(?=`\d+|$)', file_content, re.DOTALL)
                            
                            for line_range, title, description in comment_matches:
                                nitpick_comments.append({
                                    'file': file_name.strip(),
                                    'line_range': line_range.strip(),
                                    'title': title.strip(),
                                    'description': description.strip(),
                                    'full_content': f"`{line_range}`: **{title}**{description}"
                                })
    
    return nitpick_comments

def analyze_missed_nitpicks(nitpick_comments, existing_defects):
    """Analyze which nitpick comments were missed in the original defect log"""
    missed_nitpicks = []
    
    # Load existing defect log content to check descriptions
    try:
        with open('DEFECT_LOG.md', 'r') as f:
            defect_log_content = f.read()
    except FileNotFoundError:
        defect_log_content = ""
    
    for comment in nitpick_comments:
        # Check if this nitpick is already addressed
        is_addressed = False
        
        # Check by file name and line range
        file_line_pattern = f"{comment['file']}.*{comment['line_range']}"
        if re.search(file_line_pattern.replace('(', r'\(').replace(')', r'\)'), defect_log_content, re.IGNORECASE):
            is_addressed = True
        
        # Check by title/description keywords
        title_keywords = comment['title'].lower().split()[:3]  # First 3 words
        for keyword in title_keywords:
            if len(keyword) > 3 and keyword in defect_log_content.lower():
                is_addressed = True
                break
        
        if not is_addressed:
            missed_nitpicks.append(comment)
    
    return missed_nitpicks

def classify_nitpick_value(comment):
    """Classify the value/priority of a nitpick comment"""
    title = comment['title'].lower()
    description = comment['description'].lower()
    
    # High value nitpicks
    if any(keyword in title + description for keyword in [
        'security', 'vulnerability', 'strict mode', 'fail-fast', 'harden',
        'reliability', 'error handling', 'validation'
    ]):
        return 'High', 'Security/Reliability improvement'
    
    # Medium value nitpicks
    if any(keyword in title + description for keyword in [
        'best practice', 'maintainability', 'consistency', 'reproducibility',
        'pin', 'version', 'hard-coding', 'fragile'
    ]):
        return 'Medium', 'Best practices/Maintainability'
    
    # Low value nitpicks (formatting, style)
    if any(keyword in title + description for keyword in [
        'markdown', 'formatting', 'blank lines', 'md058', 'md040', 'md036',
        'yamllint', 'language specified', 'heading'
    ]):
        return 'Low', 'Code formatting/Style'
    
    return 'Low', 'General improvement'

def generate_defect_entries(missed_nitpicks, start_id=22):
    """Generate defect log entries for missed nitpicks"""
    entries = []
    current_id = start_id
    
    for comment in missed_nitpicks:
        value, category = classify_nitpick_value(comment)
        
        # Determine if we should remediate this nitpick
        should_remediate = value in ['High', 'Medium'] or (
            value == 'Low' and 'markdown' in comment['title'].lower()
        )
        
        status = 'Pending' if should_remediate else 'Evaluated - No Action'
        resolution_notes = f"Nitpick comment - {category}. " + (
            "Scheduled for remediation." if should_remediate else 
            "Low impact, no remediation needed."
        )
        
        entry = {
            'id': f'DEF-{current_id:03d}',
            'file': comment['file'],
            'line_range': comment['line_range'],
            'title': comment['title'],
            'description': comment['description'],
            'severity': 'Nitpick',
            'value': value,
            'category': category,
            'status': status,
            'resolution_notes': resolution_notes,
            'should_remediate': should_remediate
        }
        
        entries.append(entry)
        current_id += 1
    
    return entries

def main():
    """Main analysis function"""
    print("🔍 Analyzing CodeRabbit review for nitpick comments...")
    
    # Load data
    reviews = load_coderabbit_reviews()
    existing_defects = load_existing_defect_log()
    
    print(f"📊 Found {len(existing_defects)} existing defects in log")
    
    # Extract nitpick comments
    nitpick_comments = extract_nitpick_comments(reviews)
    print(f"🧹 Found {len(nitpick_comments)} total nitpick comments in CodeRabbit review")
    
    # Analyze missed nitpicks
    missed_nitpicks = analyze_missed_nitpicks(nitpick_comments, existing_defects)
    print(f"❌ Found {len(missed_nitpicks)} missed nitpick comments")
    
    if missed_nitpicks:
        print("\n📋 Missed Nitpick Comments:")
        for i, comment in enumerate(missed_nitpicks, 1):
            value, category = classify_nitpick_value(comment)
            print(f"\n{i}. {comment['file']} ({comment['line_range']})")
            print(f"   Title: {comment['title']}")
            print(f"   Value: {value} - {category}")
            print(f"   Description: {comment['description'][:100]}...")
    
    # Generate defect entries
    defect_entries = generate_defect_entries(missed_nitpicks)
    
    # Save analysis results
    analysis_results = {
        'total_nitpicks': len(nitpick_comments),
        'missed_nitpicks': len(missed_nitpicks),
        'existing_defects': len(existing_defects),
        'new_defect_entries': defect_entries,
        'analysis_date': datetime.now().isoformat()
    }
    
    with open('nitpick_analysis_results.json', 'w') as f:
        json.dump(analysis_results, f, indent=2)
    
    print(f"\n✅ Analysis complete. Results saved to nitpick_analysis_results.json")
    print(f"📈 Summary: {len(missed_nitpicks)} missed nitpicks, {sum(1 for e in defect_entries if e['should_remediate'])} recommended for remediation")
    
    return analysis_results

if __name__ == '__main__':
    results = main()
