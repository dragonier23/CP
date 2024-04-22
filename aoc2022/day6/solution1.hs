import System.IO
import Data.List
import qualified Data.Set as Set 
import Data.Char 

main = do 
    handle <- openFile "problemstatement.txt" ReadMode --"test1.txt" ReadMode --
    contents <- hGetContents handle 
    let answer = solution contents 0
    print answer
    hClose handle 

solution :: String -> Int -> Int 
solution input count 
    | repeats == 4 = count + 4
    | otherwise = solution (tail input) (count+1)
    where repeats = Set.size . Set.fromList . take 4 $ input 


