import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

data FileTree = Node (String, Int) [FileTree] [(String, Int)] deriving (Show, Read, Eq)

main = do
    handle <- openFile "problemstatement.txt" ReadMode --"test1.txt" ReadMode -- 
    contents <- hGetContents handle
    let parsedContents = parse contents
        fileTree = foldl addNode (Node (".", 0) [] []) parsedContents
        answer = solution fileTree
    print answer --fileTree --parsedContents
    hClose handle

parse :: String -> [([String], Int)]
parse = tail . foldl (\acc x -> action x acc) [([], 0)] . map words . lines

-- our file storing structure will be: [(fileAddress, size)], fileAddress = [String] (-> is increasing depth)
action :: [String] -> [([String], Int)] -> [([String], Int)]
action ["$", "cd", ".."] ((x, _):xs) = (init x, 0):xs
action ("$":"cd":a) ((x, _):xs) = (x ++ a, 0):xs
action ["$", "ls"] xs = xs
action ("dir":_) xs = xs
action [size, name] ((x, _):xs) = (x, 0):(x ++ [name], read size):xs

addNode :: FileTree -> ([String], Int) -> FileTree
addNode (Node (currDir, dirSize) childTrees files) (fileAddr, fileSize)
    | length fileAddr == 1 = let [fileName] = fileAddr
                            in Node (currDir, dirSize + fileSize) childTrees ((fileName, fileSize):files)
-- if not of length 1, then it must be in a while directory, so we must search ChildTrees 
-- 2 cases here: the child tree has / has not been created
    | foldl (\acc x -> checkNode x (head fileAddr) || acc) False childTrees =
        let updatedChildTrees = map (\x -> if checkNode x (head fileAddr) then addNode x (tail fileAddr, fileSize) else x) childTrees
        in Node (currDir, dirSize + fileSize) updatedChildTrees files
    | otherwise = Node (currDir, dirSize + fileSize) (addNode (Node (head fileAddr, 0) [] []) (tail fileAddr, fileSize):childTrees) files

checkNode :: FileTree -> String -> Bool
checkNode (Node (a, _) _ _) x
    | a == x = True
    | otherwise = False

solution :: FileTree -> Int
solution (Node (a, size) [] []) = 0
solution (Node (a, size) [] _) = if size < 100000 then size else 0
solution (Node (a, size) xs _) = (if size < 100000 then size else 0) + sum (map solution xs) 
