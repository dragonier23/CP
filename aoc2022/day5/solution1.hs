import System.IO
import Data.List
import qualified Data.Set as Set 
import Data.Char 

main = do 
    handlestack <- openFile "teststack.txt" ReadMode -- "problemstatementstack.txt" ReadMode --
    handlemoves <- openFile "testmoves.txt" ReadMode -- "problemstatementmoves.txt" ReadMode --
    contentstack <- hGetContents handlestack
    contentmoves <- hGetContents handlemoves  
    let parsedContentStack = parseStack contentstack
        parsedContentMoves = parseMoves contentmoves 
        --answer = solution parsedContents
    print parsedContents --  answer --
    hClose handle 

parseStack :: String -> [String]
parseStack = lines


solution :: [(Int, Int, Int, Int)] -> Int
solution = foldl (\acc (start1, end1, start2, end2) -> 
    let set1 = Set.fromList [start1..end1]
        set2 = Set.fromList [start2..end2]
    in if (set1 `Set.isSubsetOf` set2) || (set2 `Set.isSubsetOf` set1)
        then acc + 1 else acc) 0
