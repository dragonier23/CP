import System.IO
import Data.List
import qualified Data.Set as Set 
import Data.Char 

main = do 
    handle <- openFile  "problemstatement.txt" ReadMode --"test1.txt" ReadMode --
    contents <- hGetContents handle 
    let parsedContents = parse contents
        answer = solution parsedContents
    print answer -- parsedContents --
    hClose handle 

parse :: String -> [(Int, Int, Int, Int)]
parse = map (\line -> 
    let (x,y) = break (==',') line
        (x1, y1) = break (=='-') x
        (x2, y2) = break (=='-') $ tail y
    in (read x1 :: Int, read (tail y1) :: Int, read x2 :: Int, read (tail y2) :: Int)) . lines


solution :: [(Int, Int, Int, Int)] -> Int
solution = foldl (\acc (start1, end1, start2, end2) -> 
    let set1 = Set.fromList [start1..end1]
        set2 = Set.fromList [start2..end2]
    in if (set1 `Set.isSubsetOf` set2) || (set2 `Set.isSubsetOf` set1)
        then acc + 1 else acc) 0
