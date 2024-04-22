import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char
import Distribution.Parsec (parsecToken')

main = do
    handle <- openFile "problemstatement.txt" ReadMode --"test1.txt" ReadMode --
    contents <- hGetContents handle
    let parsedContents = parse contents
        horizontalVisible = map (\x -> xOr (line x) (reverse . line . reverse $ x)) parsedContents 
        verticalVisible = transpose $ map (\x -> xOr (line x) (reverse . line . reverse $ x)) (transpose' parsedContents)
        visible = reconcile horizontalVisible verticalVisible 
        answer = foldl (\acc x -> acc + sum x) 0 visible
    print answer
    hClose handle

--parsed :: String -> [Int]
parse :: String -> [[Int]]
parse input = map (map digitToInt) (lines input)

transpose' :: [[a]] -> [[a]]
transpose' ([]:_) = []
transpose' x = map head x: transpose' (map tail x)

line :: [Int] -> [Int]
line (x:xs) = reverse . tail . foldl (\(largest:ys) curr -> if curr > largest then curr:1:ys else largest:0:ys) [x, 1] $ xs 

xOr :: [Int] -> [Int] -> [Int]
xOr [] [] = [] 
xOr (x:xs) (y:ys) = max x y: xOr xs ys  

reconcile :: [[Int]] -> [[Int]] -> [[Int]]
reconcile [] _ = []
reconcile (x:xs) (y:ys) = xOr x y: reconcile xs ys
