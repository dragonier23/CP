import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char
import Data.Function

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsed = parse contents
        answer = solution parsed 
    print answer -- parsed --
    hClose handle

parse :: String -> 
parse = 

solution :: 
solution = 