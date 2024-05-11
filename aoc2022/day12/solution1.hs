{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use tuple-section" #-}
import System.IO
import Data.List
import qualified Data.Set as Set
import Data.Char

main = do
    handle <- openFile "test1.txt" ReadMode
    --handle <- openFile "problemstatement.txt" ReadMode
    contents <- hGetContents handle
    let parsedActions = parse contents
        (sx, sy) = parse' parsedActions 'S'
        (ex, ey) = parse' parsedActions 'E'
        start = ((length (head parsedActions) - 1) - sx, (length parsedActions - 1) - sy)
        end = ((length (head parsedActions) - 1) - ex, (length parsedActions - 1) - ey)
        toVisit = sortBy (\(_, _, d1) (_, _, d2) -> compare d1 d2) $ substitute (foldl (\acc y -> map (\x -> (x, y, 9999999)) [0..(length . head $ parsedActions)] ++ acc ) [] [0..length parsedActions]) (0, 0) (-1)
        answer = solution [] toVisit parsedActions (0, 0)
    print answer --toVisit
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
solution' :: [(Int, Int)] -> [(Int, Int, Int)] -> [String] -> (Int, Int) -> (Int, Int, Int) -> [(Int, Int, Int)]
solution' visited toVisit elevationMap (ex, ey) (x, y, dist) =
    let adjacentNodes = filter (`notElem` visited) . filter (\(cx, cy) -> cx >= 0 && cx < (length . head $ elevationMap) && cy >= 0 && cy < length elevationMap) . map (\(x, y) -> (ex + x, ey + y)) $ [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visitableAdjacentNodes = filter (\(x , y) -> let currLetter = (elevationMap !! ey) !! ex
                                                         adjLetter = (elevationMap !! y) !! x
                                                     in adjLetter == currLetter || adjLetter == succ currLetter || adjLetter == pred currLetter || adjLetter == 'E') adjacentNodes
    in  foldl (\acc x -> substitute acc x dist) toVisit visitableAdjacentNodes

substitute :: [(Int, Int, Int)] -> (Int, Int) -> Int -> [(Int, Int, Int)]
substitute [] _ _ = []
substitute ((x, y, dist):xs) (ax, ay) newDist
    | x == ax && y == ay && newDist + 1 < dist = (x, y, newDist + 1):xs
    | otherwise = (x, y, dist) : substitute xs (ax, ay) newDist

elem' :: [(Int, Int, Int)] -> (Int, Int) -> Bool
elem' xs (cx, cy) = foldl (\acc (x, y, _) -> (cx == x && cy == y) || acc) False xs