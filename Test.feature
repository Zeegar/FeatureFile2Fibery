Feature: feature 1

Scenario: scenario 1
Given step 1
When step 2
Then step 3

Scenario: scenario 2
Given step 4
When step 5
Then step 6

Scenario: scenario 3
Given step 7
When step 8
Then step 9

Scenario Outline: scenario 4
Given step 10 <column 1>
When step 11
Then step 12
Examples:
| column 1 |
| value 1  |
| value 2  |
| value 3  |

Scenario Outline: scenario 5
Given step 13
And step 14 <column 1>
When step 15
Then step 16
Examples:
| column 1 |
| value 1  |
| value 2  |

Scenario Outline: scenario 6
Given step 17
And step 18 <column 1>
When step 19
Then step 20
Examples:
| column 1 |
| value 1  |
| value 2  |

Feature: feature 2

Scenario: scenario 7
Given step 21
When step 22
Then step 23

Scenario: scenario 8
Given step 24
And step 25
When step 26
Then step 27

Scenario: scenario 9
Given step 28
And step 29
When step 30
Then step 31
And step 32

Developer Task: task 1

Feature: feature 3

Developer Task: task 2

Scenario: scenario 10
Giben step 33
When step 34
Then step 35

1Scenario: Different formatting
    Given step 36
    When step 37
    Then step 38

        Scenario: scenario 11
        Given step 39
        When step 40
        Then step 41
        And step 42


