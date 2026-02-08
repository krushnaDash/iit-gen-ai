#!/bin/bash
# Test cases for solution.py
# Run: chmod +x test_cases.sh && ./test_cases.sh

# ============ CONFIGURATION ============
PYTHON_FILE="solution.py"
# =======================================

echo "=== Testing $PYTHON_FILE ==="
echo ""

# Test 1: Sky color (Answer: A - Blue)
echo "Test 1: Sky color"
echo "Expected: A"
echo -n "Got: "
python3 $PYTHON_FILE "What color is the sky on a clear, sunny day?" "Blue" "Green" "Red" "Yellow"
echo ""

# Test 2: Sky color shuffled (Answer: B - Blue)
echo "Test 2: Sky color (shuffled options)"
echo "Expected: B"
echo -n "Got: "
python3 $PYTHON_FILE "What color is the sky on a clear, sunny day?" "Green" "Blue" "Red" "Yellow"
echo ""

# Test 3: Sky color shuffled (Answer: C - Blue)
echo "Test 3: Sky color (Blue at C)"
echo "Expected: C"
echo -n "Got: "
python3 $PYTHON_FILE "What color is the sky on a clear, sunny day?" "Green" "Red" "Blue" "Yellow"
echo ""

# Test 4: Sky color shuffled (Answer: D - Blue)
echo "Test 4: Sky color (Blue at D)"
echo "Expected: D"
echo -n "Got: "
python3 $PYTHON_FILE "What color is the sky on a clear, sunny day?" "Green" "Red" "Yellow" "Blue"
echo ""

# Test 5: Sun rises (Answer: B - East)
echo "Test 5: Where does the sun rise?"
echo "Expected: B"
echo -n "Got: "
python3 $PYTHON_FILE "Where does the sun rise?" "West" "East" "North" "South"
echo ""

# Test 6: Capital of France (Answer: A - Paris)
echo "Test 6: Capital of France"
echo "Expected: A"
echo -n "Got: "
python3 $PYTHON_FILE "What is the capital of France?" "Paris" "London" "Berlin" "Madrid"
echo ""

# Test 7: Largest planet (Answer: A - Jupiter)
echo "Test 7: Largest planet in solar system"
echo "Expected: A"
echo -n "Got: "
python3 $PYTHON_FILE "What is the largest planet in our solar system?" "Jupiter" "Saturn" "Earth" "Mars"
echo ""

# Test 8: Water formula (Answer: C - H2O)
echo "Test 8: Chemical formula of water"
echo "Expected: C"
echo -n "Got: "
python3 $PYTHON_FILE "What is the chemical formula of water?" "CO2" "NaCl" "H2O" "O2"
echo ""

# Test 9: Speed of light medium (Answer: B - Vacuum)
echo "Test 9: Speed of light fastest in"
echo "Expected: B"
echo -n "Got: "
python3 $PYTHON_FILE "In which medium does light travel fastest?" "Water" "Vacuum" "Glass" "Air"
echo ""

# Test 10: Programming language (Answer: D - Python)
echo "Test 10: Which is a programming language?"
echo "Expected: D"
echo -n "Got: "
python3 $PYTHON_FILE "Which of the following is a programming language?" "HTML" "CSS" "SQL" "Python"
echo ""

# Test 11: Boiling point of water (Answer: A - 100)
echo "Test 11: Boiling point of water in Celsius"
echo "Expected: A"
echo -n "Got: "
python3 $PYTHON_FILE "What is the boiling point of water in Celsius?" "100" "50" "0" "212"
echo ""

# Test 12: Number of continents (Answer: C - 7)
echo "Test 12: Number of continents"
echo "Expected: C"
echo -n "Got: "
python3 $PYTHON_FILE "How many continents are there on Earth?" "5" "6" "7" "8"
echo ""

# Test 13: Largest ocean (Answer: A - Pacific)
echo "Test 13: Largest ocean"
echo "Expected: A"
echo -n "Got: "
python3 $PYTHON_FILE "What is the largest ocean on Earth?" "Pacific Ocean" "Atlantic Ocean" "Indian Ocean" "Arctic Ocean"
echo ""

# Test 14: DNA stands for (Answer: B)
echo "Test 14: DNA full form"
echo "Expected: B"
echo -n "Got: "
python3 $PYTHON_FILE "What does DNA stand for?" "Deoxyribose Nucleic Acid" "Deoxyribonucleic Acid" "Dinucleotide Acid" "Dual Nucleic Acid"
echo ""

# Test 15: First President of USA (Answer: A - George Washington)
echo "Test 15: First President of USA"
echo "Expected: A"
echo -n "Got: "
python3 $PYTHON_FILE "Who was the first President of the United States?" "George Washington" "Abraham Lincoln" "Thomas Jefferson" "John Adams"
echo ""

# Test 16: Math - Square root of 144 (Answer: C - 12)
echo "Test 16: Square root of 144"
echo "Expected: C"
echo -n "Got: "
python3 $PYTHON_FILE "What is the square root of 144?" "10" "11" "12" "14"
echo ""

# Test 17: Gravity discoverer (Answer: D - Newton)
echo "Test 17: Who discovered gravity?"
echo "Expected: D"
echo -n "Got: "
python3 $PYTHON_FILE "Who is credited with discovering gravity?" "Einstein" "Galileo" "Darwin" "Newton"
echo ""

# Test 18: Capital of Japan (Answer: B - Tokyo)
echo "Test 18: Capital of Japan"
echo "Expected: B"
echo -n "Got: "
python3 $PYTHON_FILE "What is the capital of Japan?" "Seoul" "Tokyo" "Beijing" "Bangkok"
echo ""

# Test 19: Photosynthesis gas (Answer: C - Carbon dioxide)
echo "Test 19: Gas absorbed during photosynthesis"
echo "Expected: C"
echo -n "Got: "
python3 $PYTHON_FILE "What gas do plants absorb from the atmosphere during photosynthesis?" "Oxygen" "Nitrogen" "Carbon dioxide" "Hydrogen"
echo ""

# Test 20: Math 9x7 (Answer: C - 63)
echo "Test 20: 9 multiplied by 7"
echo "Expected: C"
echo -n "Got: "
python3 $PYTHON_FILE "What is 9 multiplied by 7?" "54" "56" "63" "72"
echo ""

# Test 21: FIFO data structure (Answer: B - Queue)
echo "Test 21: FIFO data structure"
echo "Expected: B"
echo -n "Got: "
python3 $PYTHON_FILE "Which data structure uses First-In-First-Out (FIFO) order?" "Stack" "Queue" "Tree" "Graph"
echo ""

# Test 22: Romeo and Juliet author (Answer: B - Shakespeare)
echo "Test 22: Romeo and Juliet author"
echo "Expected: B"
echo -n "Got: "
python3 $PYTHON_FILE "Who wrote the play 'Romeo and Juliet'?" "Charles Dickens" "William Shakespeare" "Jane Austen" "Mark Twain"
echo ""

# Test 23: Red Planet (Answer: C - Mars)
echo "Test 23: Red Planet"
echo "Expected: C"
echo -n "Got: "
python3 $PYTHON_FILE "Which planet is known as the Red Planet?" "Earth" "Venus" "Mars" "Jupiter"
echo ""

# Test 24: Ripe banana color (Answer: D - Yellow)
echo "Test 24: Ripe banana color"
echo "Expected: D"
echo -n "Got: "
python3 $PYTHON_FILE "What color is a ripe banana?" "Red" "Blue" "Green" "Yellow"
echo ""

echo ""
echo "=== All tests completed ==="
