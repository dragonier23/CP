import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    --handle <- openFile "test1.txt" ReadMode
    handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsedActions = parse contents
        (sx, sy) = parse' parsedActions 'S'
        (ex, ey) = parse' parsedActions 'E'
        start = ((length (head parsedActions) - 1) - sx, (length parsedActions - 1) - sy)
        end = ((length (head parsedActions) - 1) - ex, (length parsedActions - 1) - ey)
        toVisit = sortBy (\(_, _, d1) (_, _, d2) -> compare d1 d2) $ substitute (foldl (\acc y -> map (\x -> (x, y, 9999999)) [0..((length . head $ parsedActions) - 1)] ++ acc ) [] [0..length parsedActions - 1]) start (-1)
        --answer = solution' [] toVisit parsedActions end (59, 20, 340) --(58, 20)
        answer = solution [] toVisit parsedActions end
    print answer --toVisit --
    hClose handle

parse :: String -> [String]
parse = lines

parse' :: [String] -> Char -> (Int, Int)
parse' [] _ = (-1, -1)
parse' ([]:ys) toFind = parse' ys toFind
parse' ((x:xs):ys) toFind
    | x == toFind = (length xs, length ys)
    | otherwise = parse' (xs:ys) toFind

-- this will be a classic djikstra -> we will have a list of unvisited nodes, type [(x, y, dist)]
-- the steps will to have this whole list of unvisited nodes, and the first one is the curr -> find the next adjacent nodes that we can visit
-- if the curr node is the end node, we should aim to return its dist
-- else, we should find the adjacent nodes. find if 1. visitable 2. visited alr 3. then update the distance -> remove the node, and add the node with
-- the updated node, then sort it 
-- so we will use a fold?

solution :: [(Int, Int)] -> [(Int, Int, Int)] -> [String] -> (Int, Int) -> Int
solution _ [] _ _ = -1
solution visited ((x, y, dist):xs) elevationMap (ex, ey)
    | x == ex && y == ey = dist
    | otherwise = solution ((x, y):visited) updatedxs elevationMap (ex, ey)
    where updatedxs = sortBy (\(_, _, d1) (_, _, d2) -> compare d1 d2) $ solution' visited xs elevationMap (ex, ey) (x, y, dist)

-- updatedxs needs to be sorted too 
-- input is: visited, tovisit, elevationmap, endloc, currloc + dist
solution' :: [(Int, Int)] -> [(Int, Int, Int)] -> [String] -> (Int, Int) -> (Int, Int, Int) -> [(Int, Int, Int)]
solution' visited toVisit elevationMap (ex, ey) (cx, cy, dist) =
    let adjacentNodes = filter (`notElem` visited) . filter (\(ax, ay) -> ax >= 0 && ax < (length . head $ elevationMap) && ay >= 0 && ay < length elevationMap) . map (\(x, y) -> (cx + x, cy + y)) $ [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visitableAdjacentNodes = filter (\(x , y) -> let currLetter = (elevationMap !! cy) !! cx
                                                         adjLetter = (elevationMap !! y) !! x
                                                     in adjLetter `elem` ['a'..succ currLetter] || (adjLetter == 'E' && (currLetter == 'z' || currLetter == 'y')) || (currLetter == 'S' && (adjLetter == 'a' || adjLetter == 'b'))) adjacentNodes
    in foldl (\acc x -> substitute acc x dist) toVisit visitableAdjacentNodes

substitute :: [(Int, Int, Int)] -> (Int, Int) -> Int -> [(Int, Int, Int)]
substitute [] _ _ = []
substitute ((x, y, dist):xs) (ax, ay) newDist
    | x == ax && y == ay && newDist + 1 < dist = (x, y, newDist + 1):xs
    | otherwise = (x, y, dist) : substitute xs (ax, ay) newDist