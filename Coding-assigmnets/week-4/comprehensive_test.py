"""
Comprehensive Test Suite for MCQ Template
Tests with high variance across multiple domains and question types.
"""

import subprocess
import sys
import time

# Comprehensive test cases across various domains
test_cases = [
    # === ORIGINAL ASSIGNMENT TESTS ===
    ("Sky color (A)", "What color is the sky on a clear, sunny day?", "Blue", "Green", "Red", "Yellow", "A"),
    ("Sky color (B)", "What color is the sky on a clear, sunny day?", "Green", "Blue", "Red", "Yellow", "B"),
    ("Sky color (C)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Blue", "Yellow", "C"),
    ("Sky color (D)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Yellow", "Blue", "D"),
    
    # === SCIENCE & NATURE ===
    ("Water formula", "What is the chemical formula for water?", "H2O", "CO2", "NaCl", "O2", "A"),
    ("Speed of light", "What travels at approximately 300,000 km/s?", "Sound", "Light", "Electricity", "Wind", "B"),
    ("DNA shape", "What is the shape of DNA?", "Circle", "Square", "Double helix", "Triangle", "C"),
    ("Photosynthesis output", "What do plants produce during photosynthesis?", "Carbon dioxide", "Nitrogen", "Water", "Oxygen", "D"),
    ("Boiling point water", "At what temperature does water boil at sea level?", "100°C", "0°C", "50°C", "212°F only", "A"),
    ("Largest planet", "Which is the largest planet in our solar system?", "Saturn", "Jupiter", "Neptune", "Uranus", "B"),
    ("Noble gas", "Which of these is a noble gas?", "Oxygen", "Nitrogen", "Helium", "Hydrogen", "C"),
    ("Red Planet", "Which planet is known as the Red Planet?", "Venus", "Jupiter", "Saturn", "Mars", "D"),
    
    # === MATHEMATICS ===
    ("2+2", "What is 2 + 2?", "4", "3", "5", "6", "A"),
    ("Square root 144", "What is the square root of 144?", "10", "12", "14", "11", "B"),
    ("Pi value", "What is the approximate value of pi?", "2.14", "4.14", "3.14", "1.14", "C"),
    ("Prime number", "Which of these is a prime number?", "4", "6", "8", "7", "D"),
    ("Pythagorean theorem", "In a right triangle, what does a² + b² equal?", "c²", "2c", "c", "ab", "A"),
    ("Fraction to decimal", "What is 1/4 as a decimal?", "0.5", "0.25", "0.75", "0.125", "B"),
    
    # === GEOGRAPHY ===
    ("Capital France", "What is the capital of France?", "Paris", "London", "Berlin", "Rome", "A"),
    ("Longest river", "What is the longest river in the world?", "Amazon", "Nile", "Mississippi", "Yangtze", "B"),
    ("Largest ocean", "What is the largest ocean on Earth?", "Atlantic", "Indian", "Pacific", "Arctic", "C"),
    ("Mount Everest location", "In which mountain range is Mount Everest located?", "Andes", "Alps", "Rocky Mountains", "Himalayas", "D"),
    ("Country continent", "Which continent is Australia in?", "Australia/Oceania", "Asia", "Europe", "Africa", "A"),
    ("Largest desert", "What is the largest hot desert in the world?", "Gobi", "Sahara", "Arabian", "Kalahari", "B"),
    
    # === HISTORY ===
    ("First US President", "Who was the first President of the United States?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams", "A"),
    ("WWII end year", "In what year did World War II end?", "1944", "1945", "1946", "1943", "B"),
    ("Ancient wonder", "The Great Pyramid is located in which country?", "Iraq", "Greece", "Egypt", "Italy", "C"),
    ("Moon landing year", "In what year did humans first land on the Moon?", "1967", "1968", "1970", "1969", "D"),
    
    # === LITERATURE & ARTS ===
    ("Romeo Juliet author", "Who wrote Romeo and Juliet?", "William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain", "A"),
    ("Mona Lisa artist", "Who painted the Mona Lisa?", "Michelangelo", "Leonardo da Vinci", "Raphael", "Van Gogh", "B"),
    ("1984 author", "Who wrote the novel '1984'?", "Aldous Huxley", "Ray Bradbury", "George Orwell", "H.G. Wells", "C"),
    ("Starry Night artist", "Who painted 'The Starry Night'?", "Monet", "Picasso", "Rembrandt", "Van Gogh", "D"),
    
    # === BIOLOGY ===
    ("Largest organ", "What is the largest organ in the human body?", "Skin", "Liver", "Heart", "Brain", "A"),
    ("Blood type universal", "Which blood type is known as the universal donor?", "A", "O negative", "B", "AB positive", "B"),
    ("Human chromosomes", "How many chromosomes do humans have?", "23", "44", "46", "48", "C"),
    ("Vitamin D source", "Which vitamin is primarily obtained from sunlight?", "Vitamin A", "Vitamin C", "Vitamin B12", "Vitamin D", "D"),
    
    # === TECHNOLOGY & COMPUTING ===
    ("Binary base", "What base is the binary number system?", "Base 2", "Base 8", "Base 10", "Base 16", "A"),
    ("WWW inventor", "Who is credited with inventing the World Wide Web?", "Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Mark Zuckerberg", "B"),
    ("RAM meaning", "What does RAM stand for in computing?", "Read Access Memory", "Remote Access Memory", "Random Access Memory", "Run Access Memory", "C"),
    ("First computer", "What was the name of the first electronic general-purpose computer?", "UNIVAC", "IBM PC", "Apple I", "ENIAC", "D"),
    
    # === LANGUAGE & GRAMMAR ===
    ("Noun definition", "What part of speech names a person, place, or thing?", "Noun", "Verb", "Adjective", "Adverb", "A"),
    ("Plural of child", "What is the plural of 'child'?", "Childs", "Children", "Childes", "Child", "B"),
    ("Opposite of hot", "What is the antonym of 'hot'?", "Warm", "Burning", "Cold", "Tepid", "C"),
    ("Homophone of 'there'", "Which word sounds the same as 'there'?", "Here", "Where", "Hear", "Their", "D"),
    
    # === TRICKY/EDGE CASES ===
    ("Trick question 1", "How many months have 28 days?", "All 12", "1", "2", "None", "A"),
    ("Common knowledge", "What color is a banana when it's ripe?", "Green", "Yellow", "Red", "Blue", "B"),
    ("Simple logic", "If all cats are animals, and Whiskers is a cat, what is Whiskers?", "A plant", "A mineral", "An animal", "A fungus", "C"),
    ("Basic fact", "How many days are in a week?", "5", "6", "8", "7", "D"),
]

# Test cases from test_cases.sh
shell_test_cases = [
    ("Shell: Sky color (A)", "What color is the sky on a clear, sunny day?", "Blue", "Green", "Red", "Yellow", "A"),
    ("Shell: Sky color (B)", "What color is the sky on a clear, sunny day?", "Green", "Blue", "Red", "Yellow", "B"),
    ("Shell: Sky color (C)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Blue", "Yellow", "C"),
    ("Shell: Sky color (D)", "What color is the sky on a clear, sunny day?", "Green", "Red", "Yellow", "Blue", "D"),
    ("Shell: Sun rises", "Where does the sun rise?", "West", "East", "North", "South", "B"),
    ("Shell: Capital France", "What is the capital of France?", "Paris", "London", "Berlin", "Madrid", "A"),
    ("Shell: Largest planet", "What is the largest planet in our solar system?", "Jupiter", "Saturn", "Earth", "Mars", "A"),
    ("Shell: Water formula", "What is the chemical formula of water?", "CO2", "NaCl", "H2O", "O2", "C"),
    ("Shell: Speed of light", "In which medium does light travel fastest?", "Water", "Vacuum", "Glass", "Air", "B"),
    ("Shell: Programming lang", "Which of the following is a programming language?", "HTML", "CSS", "SQL", "Python", "D"),
    ("Shell: Boiling point", "What is the boiling point of water in Celsius?", "100", "50", "0", "212", "A"),
    ("Shell: Continents", "How many continents are there on Earth?", "5", "6", "7", "8", "C"),
    ("Shell: Largest ocean", "What is the largest ocean on Earth?", "Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "A"),
    ("Shell: DNA full form", "What does DNA stand for?", "Deoxyribose Nucleic Acid", "Deoxyribonucleic Acid", "Dinucleotide Acid", "Dual Nucleic Acid", "B"),
    ("Shell: First US President", "Who was the first President of the United States?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams", "A"),
    ("Shell: Square root 144", "What is the square root of 144?", "10", "11", "12", "14", "C"),
    ("Shell: Gravity discoverer", "Who is credited with discovering gravity?", "Einstein", "Galileo", "Darwin", "Newton", "D"),
    ("Shell: Capital Japan", "What is the capital of Japan?", "Seoul", "Tokyo", "Beijing", "Bangkok", "B"),
    ("Shell: Photosynthesis gas", "What gas do plants absorb from the atmosphere during photosynthesis?", "Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen", "C"),
    ("Shell: 9x7", "What is 9 multiplied by 7?", "54", "56", "63", "72", "C"),
    ("Shell: FIFO structure", "Which data structure uses First-In-First-Out (FIFO) order?", "Stack", "Queue", "Tree", "Graph", "B"),
    ("Shell: Romeo Juliet", "Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", "B"),
    ("Shell: Red Planet", "Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", "C"),
    ("Shell: Ripe banana", "What color is a ripe banana?", "Red", "Blue", "Green", "Yellow", "D"),
]

def run_test(name, question, opt_a, opt_b, opt_c, opt_d, expected):
    """Run template.py with given inputs and return result."""
    cmd = [
        sys.executable, "template.py",
        question, opt_a, opt_b, opt_c, opt_d
    ]
    try:
        start_time = time.time()
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        elapsed_time = time.time() - start_time
        output = result.stdout.strip()
        # Get the last line (in case there's any other output)
        output = output.split('\n')[-1].strip() if output else ""
        stderr = result.stderr.strip() if result.stderr else ""
        return output, elapsed_time, stderr
    except subprocess.TimeoutExpired:
        return "TIMEOUT", 600.0, ""
    except Exception as e:
        return f"ERROR: {e}", 0.0, ""

def run_test_suite(test_list, suite_name, categories=None):
    """Run a test suite and return results."""
    print("=" * 100)
    print(f"{suite_name}")
    print(f"Total Test Cases - : {len(test_list)}")
    print("=" * 100)
    
    results = []
    passed = 0
    total_time = 0.0
    
    for i, (name, question, opt_a, opt_b, opt_c, opt_d, expected) in enumerate(test_list, 1):
        print(f"\n[{i}/{len(test_list)}] Testing: {name}...")
        print(f"    Q: {question[:60]}{'...' if len(question) > 60 else ''}")
        
        output, elapsed, stderr = run_test(name, question, opt_a, opt_b, opt_c, opt_d, expected)
        total_time += elapsed
        
        status = "PASS" if output == expected else "FAIL"
        if output == expected:
            passed += 1
            
        results.append((name, expected, output, status, elapsed))
        symbol = "✅" if status == "PASS" else "❌"
        print(f"    Expected: {expected} | Got: {output} | {symbol} {status} ({elapsed:.2f}s)")
        
        if stderr and "WARNING" not in stderr.upper():
            print(f"    ⚠️  Stderr: {stderr[:100]}")
    
    # Print detailed results table
    print("\n" + "=" * 100)
    print(f"DETAILED RESULTS TABLE - {suite_name}")
    print("=" * 100)
    print(f"{'#':<4} {'Test Name':<35} {'Expected':<10} {'Got':<10} {'Time(s)':<10} {'Status':<10}")
    print("-" * 100)
    
    for i, (name, expected, got, status, elapsed) in enumerate(results, 1):
        symbol = "✅" if status == "PASS" else "❌"
        print(f"{i:<4} {name:<35} {expected:<10} {got:<10} {elapsed:<10.2f} {symbol} {status}")
    
    # Category breakdown if provided
    if categories:
        print("\n" + "=" * 100)
        print(f"CATEGORY BREAKDOWN - {suite_name}")
        print("=" * 100)
        print(f"{'Category':<30} {'Passed':<15} {'Percentage':<15}")
        print("-" * 60)
        
        for cat_name, (start, end) in categories.items():
            cat_results = results[start:end]
            cat_passed = sum(1 for r in cat_results if r[3] == "PASS")
            cat_total = len(cat_results)
            percentage = (cat_passed / cat_total * 100) if cat_total > 0 else 0
            status_emoji = "✅" if cat_passed == cat_total else "⚠️" if cat_passed > 0 else "❌"
            print(f"{cat_name:<30} {cat_passed}/{cat_total:<12} {percentage:>6.1f}% {status_emoji}")
    
    # Failed tests summary
    failed_tests = [(i+1, r) for i, r in enumerate(results) if r[3] == "FAIL"]
    if failed_tests:
        print("\n" + "=" * 100)
        print(f"FAILED TESTS DETAILS - {suite_name}")
        print("=" * 100)
        for idx, (name, expected, got, status, elapsed) in failed_tests:
            tc = test_list[idx-1]
            print(f"\n❌ Test #{idx}: {name}")
            print(f"   Question: {tc[1]}")
            print(f"   Options: A={tc[2]}, B={tc[3]}, C={tc[4]}, D={tc[5]}")
            print(f"   Expected: {expected}, Got: {got}")
    
    # Suite summary
    print("\n" + "=" * 100)
    print(f"SUMMARY - {suite_name}")
    print("=" * 100)
    print(f"Total Tests:     {len(test_list)}")
    print(f"Passed:          {passed}")
    print(f"Failed:          {len(test_list) - passed}")
    print(f"Pass Rate:       {passed/len(test_list)*100:.1f}%")
    print(f"Total Time:      {total_time:.2f}s")
    print(f"Average Time:    {total_time/len(test_list):.2f}s per test")
    print("=" * 100)
    
    return results, passed, total_time

def main():
    # Category tracking for comprehensive tests
    categories = {
        "Original Assignment": (0, 4),
        "Science & Nature": (4, 12),
        "Mathematics": (12, 18),
        "Geography": (18, 24),
        "History": (24, 28),
        "Literature & Arts": (28, 32),
        "Biology": (32, 36),
        "Technology & Computing": (36, 40),
        "Language & Grammar": (40, 44),
        "Tricky/Edge Cases": (44, 48),
    }
    
    # Run Comprehensive Test Suite
    comp_results, comp_passed, comp_time = run_test_suite(
        test_cases, 
        "COMPREHENSIVE MCQ TEST SUITE", 
        categories
    )
    
    print("\n" + "🔹" * 50 + "\n")
    
    # Run Shell Test Cases Suite
    shell_results, shell_passed, shell_time = run_test_suite(
        shell_test_cases, 
        "SHELL TEST CASES (from test_cases.sh)"
    )
    
    # Combined Results
    total_tests = len(test_cases) + len(shell_test_cases)
    total_passed = comp_passed + shell_passed
    total_time = comp_time + shell_time
    
    print("\n" + "🔸" * 50 + "\n")
    print("=" * 100)
    print("COMBINED FINAL SUMMARY")
    print("=" * 100)
    print(f"\n{'Suite':<40} {'Passed':<15} {'Total':<10} {'Pass Rate':<15} {'Time':<10}")
    print("-" * 100)
    print(f"{'Comprehensive Tests':<40} {comp_passed:<15} {len(test_cases):<10} {comp_passed/len(test_cases)*100:.1f}%{'':<9} {comp_time:.2f}s")
    print(f"{'Shell Test Cases':<40} {shell_passed:<15} {len(shell_test_cases):<10} {shell_passed/len(shell_test_cases)*100:.1f}%{'':<9} {shell_time:.2f}s")
    print("-" * 100)
    print(f"{'COMBINED TOTAL':<40} {total_passed:<15} {total_tests:<10} {total_passed/total_tests*100:.1f}%{'':<9} {total_time:.2f}s")
    print("=" * 100)
    
    print(f"\n📊 Overall Statistics:")
    print(f"   Total Tests:     {total_tests}")
    print(f"   Total Passed:    {total_passed}")
    print(f"   Total Failed:    {total_tests - total_passed}")
    print(f"   Overall Rate:    {total_passed/total_tests*100:.1f}%")
    print(f"   Total Time:      {total_time:.2f}s")
    print(f"   Average Time:    {total_time/total_tests:.2f}s per test")
    print("=" * 100)
    
    # Exit code based on results
    if total_passed == total_tests:
        print("\n🎉 ALL TESTS PASSED! Your implementation looks solid.")
        return 0
    elif total_passed >= total_tests * 0.9:
        print(f"\n⚠️  {total_tests - total_passed} test(s) failed. Minor issues to fix.")
        return 1
    else:
        print(f"\n❌ {total_tests - total_passed} test(s) failed. Review your implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
