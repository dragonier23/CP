import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char
import Data.Function

data Tree = EmptyTree | Packets Int | Node [Tree] deriving (Show, Read, Eq)

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsed = parse contents
        answer = solution parsed 
    print answer -- parsed --
    hClose handle

parse :: String -> [[Tree]]
parse = map (map (parse' . init . tail)) . filter (\x -> 2 == length x) . groupBy ((==) `on` null) . lines

-- if we think about it, [] contains either lone numbers or lists of list -> we should identify where the brackets start and end, then
-- use that information to craft the tree
-- we need to take note if the number is 10 
parse' :: String -> Tree
parse' [] = EmptyTree
parse' xs =
    let subTrees = findSubTree xs
        (index, Node tree) = foldl (\(index, Node t) x -> if isDigit x && not (inSubTree subTrees index) then 
                                            (if x == '1' && (index + 1) < length xs then 
                                                (if xs !! (index + 1) == '0' then (index + 1, Node (Packets 10:t)) else (index + 1, Node (Packets (digitToInt x):t)))
                                                else (if x == '0' && index > 0 then (if xs !! (index -1) == '1' then (index + 1, Node t) else (index + 1, Node (Packets (digitToInt x):t))) else (index + 1, Node (Packets (digitToInt x):t))))
                                            else (if not . null . isSubTree subTrees $ index then let [(s, e)] = isSubTree subTrees index
                                                                                                  in (index + 1, Node (parse' (drop (s+1) . take e $ xs):t))
                                            else (index + 1, Node t))) (0, Node []) xs -- acc is (index, Tree) 
    in Node (reverse tree)


findSubTree :: String -> [(Int, Int)]
findSubTree = subTreesRange . reverse . drop 2 . foldl (\(depth:index:xs) x ->
    if x == '[' && depth == 0 then (depth+1):(index+1):index:xs
    else (if x == ']' && depth == 1 then (depth-1):(index+1):index:xs
    else (if x == '[' then (depth+1):(index+1):xs
    else (if x == ']' then (depth-1):(index+1):xs else depth:(index+1):xs)))) [0, 0]


subTreesRange :: [Int] -> [(Int, Int)]
subTreesRange [] = []
subTreesRange (x:y:xs) = (x, y):subTreesRange xs

inSubTree :: [(Int, Int)] -> Int -> Bool
inSubTree xs index = foldl (\acc (s, e) -> (index >= s && index <= e) || acc) False xs

isSubTree :: [(Int, Int)] -> Int -> [(Int, Int)]
isSubTree xs index = foldl (\acc (s, e) -> if index == s then [(s, e)] else acc) [] xs

solution :: [[Tree]] -> Int
solution = sum . foldl (\acc x -> if x == 1 then length acc + 1 : acc else 0:acc) []. map (\[leftTree, rightTree] -> solution' leftTree rightTree)

-- Tree is made of Packets and other Trees: we need a function to compare to equivalent things, since it is in order 
solution' :: Tree -> Tree -> Int
solution' (Packets left) (Packets right)
    | left < right = 1
    | left > right = 0
    | left == right = -1
solution' EmptyTree EmptyTree = -1
solution' EmptyTree (Packets _) = 1
solution' (Packets _) EmptyTree = 0
solution' EmptyTree (Node _) = 1
solution' (Node _) EmptyTree = 0
solution' (Packets left) (Node right) = solution' (Node [Packets left]) (Node right)
solution' (Node left) (Packets right) = solution' (Node left) (Node [Packets right]) 
solution' (Node ls) (Node rs) -- in the case we have 2 list, we need to compare the 2 list's elements 
    | eval == (-1) && length ls < length rs = 1
    | eval == (-1) && length ls > length rs = 0
    | eval == (-1) && length ls == length rs = -1
    | otherwise = eval
    where zipped = zip ls rs
          eval = foldl (\acc (left, right) -> if solution' left right == 1 && acc == (-1) then 1
                                              else (if solution' left right == 0 && acc == (-1) then 0
                                              else acc)) (-1) zipped

    -- we should zip them, then compare them
