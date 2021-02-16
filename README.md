# FYP-COMP30910-MSCP #

## Final Year Project (FYP) Title: *'Finding the Minimum Number of Sudoku Clues Through Information Theory'* ##
Completed my final year project under the supervision of Félix Balado Pumariño, over the course of two modules totalling 15 credits due to University College Dublin’s new FYP structure: Final Year Project Foundations (COMP30900) at 5 credits and Final Year Project Design and Implementation (COMP30910) at 10 credits. 

### Final Year Project Foundations (COMP30900) ###
* __Wrote foundations report (28 pages)__ under the following headings; Abstract, Introduction, Groundwork, Data Considerations, Outline of Approach, Summary and Conclusions, Acknowledgements and Bibliography

* Gave a 10-minute presentation on my final year project to my two assigned moderators; Damian Dalton and Shen Wang. 

### Final Year Project Design and Implementation (COMP30910) ###
* __Wrote final report (39 pages)__ under the following headings; List of Figures, List of Tables, Glossary, Abstract, Introduction, Project Specification, Groundwork, Data & Context, Core Contribution, Evaluation, Summary and Conclusions, Acknowledgements, Appendices and Bibliography

## Abstract ##

Sudoku is a puzzle game where the player is presented with a 9 x 9 square grid called a Sudoku grid such that every row, column, and 3 x 3 square subgrid contain a permutation of the numbers 1 to 9. In a Sudoku puzzle, a few squares out of the 81 forming a chosen Sudoku grid are given as clues to the player, who has to guess the content of the remaining ones. In 2013, McGuire et al. found through a mathematically informed empirical search that 17 is the minimum number of clues for a Sudoku puzzle to be uniquely solvable. However, there is no formula yet that tells us why this should be so. This research project aims to investigate the Minimum Number of Clues for a Sudoku puzzle to be uniquely solvable from a theoretical perspective; using the tools of Information Theory to model Sudoku as an erasure channel in an effort to produce theoretical results that can give insight into why exactly it is that 17 is the minimum number of clues for a Sudoku puzzle to be uniquely solvable.

#### __Description__ ####

A Sudoku grid is a 9x9 square grid such that every row, column, and 3x3
square subgrid contain a permutation of the numbers 1 to 9.

In a Sudoku puzzle, a few squares out of the 81 forming a chosen Sudoku
grid are given as clues to the player, who has to guess the content of the
remaining ones. In 2013, McGuire et al found through a mathematically-
informed empirical search that 17 is the minimum number of clues for a
Sudoku puzzle to be uniquely solvable. However there is no formula yet
that tells us why this should be so.

#### __Core__ ####

Firstly, the student will become acquainted with Sudoku and its most
relevant literature. A Sudoku grid can be seen as a 9-ary code where only
certain codewords are allowed. Thus a Sudoku puzzle can be seen as
putting a Sudoku grid (codeword) through a 9-ary erasure communications
channel. The task of the player is to _decode_ the original codeword (i.e. the
original grid) from the noisy output of the channel. Since it is known how
many Sudoku grids exist (i.e., the number of Sudoku grids has been
enumerated), the rate of the code is also known.

For this reason, information theory should be able to allow us to investigate
the minimum number of clues in an analytical way. With the help of the
advisor, the student will study the problem from the point of view of
standard information theory, where the uses of the channel go
asymptotically to infinity.

#### __Advanced__ ####
To refine the results above it will be necessary to resort to zero-error
capacity in the erasure channel, over an infinite number of channel uses (i.e.,
81 uses).

#### __Dataset__ ####

Catalogue of known Sudoku grids

#### __Requirements__ ####

Strong interest in information theory, and not afraid of a challenge.






