import System.IO
import Data.List

main = do 
    handle <- openFile "problemstatement.txt" ReadMode --"test1.txt" ReadMode -- 
    contents <- hGetContents handle 
    let parsedContents = parse contents
        answer = solution parsedContents
    print answer
    hClose handle 

parse :: String -> [(Char, Char)]
parse = map (\moves -> ((moves !! 0, moves !! 2))) . lines


solution :: (Num a) => [(Char, Char)] -> a 
solution = sum . map game 

game :: (Num a) => (Char, Char) -> a 
game ('A', 'X') = 4
game ('A', 'Y') = 8
game ('A', 'Z') = 3
game ('B', 'X') = 1
game ('B', 'Y') = 5
game ('B', 'Z') = 9
game ('C', 'X') = 7
game ('C', 'Y') = 2
game ('C', 'Z') = 6