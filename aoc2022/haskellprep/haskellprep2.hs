-- to import stuff, 
import Data.List -- can end with certain functions wrapped in parentheses. if overlapping, use 
-- qualified import, i.e. import qualified Data.Map as M
-- to use in GHCI: :m + (module names)
import Data.Char
import qualified Data.Map as Map
import qualified Data.Set as Set
import HaskellPrep3

-- Potentially useful functions:

-- Data.List
-- nub: takes a list and weeds out duplicates
-- intersperse
-- intercalate 
-- transpose 
-- concat
-- concatMap
-- and, or, any, all
-- iterate 
-- splitAt, takeWhile, dropWhile, span, break 
-- sort 
-- group, groupBy (takes a predicate)
-- inits, tails 
search :: (Eq a) => [a] -> [a] -> Bool
search toFind array =
    let nlength = length toFind
    in foldl (\acc x -> take nlength x == toFind || acc) False (tails array)
-- this is an implementation of the function isInfixOf, which there are the variations isPrefixOf and isSuffixOf
-- elem, notElem
-- partition
-- find -> note it returns a Maybe value, takes a predicate and a list
-- elemIndex, elemIndicies
-- findIndex, findIndices 
-- zip3, zip4 ... zip7
-- ****lines -> convert text to array (split by \n) ****, unlines vice versa 
-- delete
-- \\ for difference between 2 sets 
-- union
-- insert
on' :: (b -> b -> c) -> (a -> b) -> a -> a -> c
f `on'` g = \x y -> f (g x) (g y)
-- for groupBy / sortBy -> sortBy (compare `on` length) xs AND groupBy ((==) `on` (>0)) xs 
-- can be read as: sort by comparing the length of each element of xs
-- OR group the array by whether its elements are greater than 0 or not

-- Data.Char
-- isControl, isSpace, isLower, isUpper, isAlpha, isAlphaNUm, isPrint, isDigit, isOctDigit, isHexDigit
-- isLetter, isMark, isPunctuation, isSymbol, isSeperator, isAscii, isLatin1, isAsciiUpper, isAsciiLower 
-- mostly Char -> Bool 
-- generalCategory -> for getting the category of the character 
-- toUpper, toLower, toTitle, digitToInt, intToDigit
-- ord, chr -> change from char to number (ASCII VALUE)
encode :: Int -> String -> String -- caeser cipher
encode shift = map (\x -> chr . (+) shift . ord $ x)

-- Data.Map
-- hashmaps
findKey :: (Eq k) => k -> [(k, v)] -> Maybe v
findKey _ [] = Nothing
findKey key ((k, v):xs)
    | key == k = Just v
    | otherwise = findKey key xs

findKey' :: (Eq k) => k -> [(k, v)] -> Maybe v
findKey' key = foldl (\acc (k, v) -> if key == k then Just v else acc) Nothing
-- fromList -> takes list and convert to map  - duplicate keys are discarded 
-- Note that the hashmap is implemented as a Tree, hence, keys must be orderable
-- Map.empty -> empty Mapping
-- Map.insert , null, size, singleton, member, map, filter, toList (from mpaping to list)
-- keys (same as map fst), elems (same as map snd)
-- insertWith
-- fromListWith (allows you to decide what to do with duplicate keies)
-- Data.Map.fromListWith :: Ord k => (a -> a -> a) -> [(k, a)] -> Map k a
phoneBookToMap :: (Ord k) => [(k, String)] -> Map.Map k String
phoneBookToMap = Map.fromListWith (\number1 number2 -> number1 ++ ", " ++ number2)

max''' :: (Ord k) => [(k, String)] -> Map.Map k String
max''' = Map.fromListWith max

-- Data.Set
-- also has fromList, 
-- difference (in first set but not in second)
-- intersection, union, null, size, singlton, insert, delete
-- isSubsetOf, isProperSubsetOf 
-- filter, map, toList



-- Making our own datatypes: 
-- data (type constructor, type parameters) = (value constructors, value parameters) | (value constructors, value parameters)
-- we can think of the value constructor as a function that either strings together multiple 
-- pieces of data, or some value that has meaning in and of itself 
-- In other words, value constructors are just functions that take the fields as parameters and 
-- return a value of some type (like Shape) as a result
-- for instance 
data Shape = Circle Float Float Float | Rectangle Float Float Float Float deriving (Show)
-- deriving adds this data type to a typeclass
-- we can use this in our functions
surface :: Shape -> Float
surface (Circle _ _ r) = pi * r ^ 2
surface (Rectangle x1 x2 y1 y2) = abs $ (y2 - y1) * (x1 - x2)

-- we could also define shape as
data Point = Point Float Float deriving (Show)
data Shape' = Circle' Point Float | Rectangle' Point Point
surface' :: Shape' -> Float
surface' (Circle' _ r) = pi * r ^ 2
surface' (Rectangle' (Point x1 y1) (Point x2 y2)) = abs (x2 - x1) * abs (y2 - y1)
-- We use the same name for the data type and the value constructor, we should do this if theres only
-- 1 value constructor 
-- Note that we are able to pattern match in this case. 
-- we can similarly export these data types, with: 
-- module Shapes (Points(..), Shape(Rectangle, Circke), surface)
-- notes the ".." allows us to export all value constructors for Point, in this case just Point
-- if we are to just write Shape, it will allow us to use the type Shape in functions, but be unable to construct 
-- its value ourselves 
-- Note however that we will be unable to pattern match against the value constructor

-- This is done for Map, where we are unable to call the Map value constructor

-- Having the value constructor like this can be confusing, hence, we have 
data Person = Person {
    firstName :: String,
    lastName :: String, 
    age :: Int
}

-- this gives us the functions firstName, lastName and age, which we can 
-- :t firstName
-- firstName :: Person -> String 

-- To define a person, we have 
-- Person {firstName="Jerry", lastName="Tan", age="60"} - pattern matching with this would be similar 

-- we look at type constructors 
data Maybe' a = Nothing' | Maybe' a 
-- we could redefine person as 
data Person' a b c = Person' {
    firstName' :: a,
    secondName' :: b,
    age' :: c
} deriving (Eq)

-- the types of all  fields also have to be part of the Eq typeclass 

-- we can also add a typeclass constraint in the definition 
-- This is almost never done though
-- we could do: data (Num a) => Vector a = Vector a a a deriving (Show) 
-- but this would require all our functions to have this constraint even when it dosent matter
-- Hence, we just do data Vector a = Vector a a a deriving (Show)
-- and add the Num typeclass in the functions that follow  

-- Ord typeclass - if we compare 2 values of the same type that were made with different
-- constructors, the one that was defined first is considered smaller 
-- Enum will allow us to utilise texas ranges, showing everything between 

-- For clarity, we can use type synonyms. For instance
type String' = [Char]
-- type synonyms can also be parameterised
type AssocList k v = [(k, v)]
-- Another data type
-- data Either a b = Left a | Right b deriving (Show, Read, Ord, Eq)
-- can be a useful tool for returning error messages (as opposed to maybe which dosent tell us much info)
-- error use left, results use right 

data LockerState = Taken | Free deriving (Show, Eq)
type Code = String
type LockerMap = Map.Map Int (LockerState, Code)

lockerLookup :: Int -> LockerMap -> Either String String 
lockerLookup lookupCode lockerMap = 
    case Map.lookup lookupCode lockerMap of 
        Nothing -> Left "HELP"
        Just (lockerState, code) -> if lockerState == Taken then Left "Taken" else Right code

--    | Map.member lookupCode lockerMap == False = Left "does not exist"
  --  | otherwise = let Just (lockerState, code) = Map.lookup lookupCode lockerMap 
    --              in if lockerState == Taken 
      --               then Left "TAKEN" 
        --             else Right code

-- we can also define values to be recursive 
data List a = Empty | Link a (List a) deriving (Eq, Show, Read, Ord)
-- we could also define it as: data List a = Empty | Link {listHead :: a, listTail :: (List a)} 
-- deriving (Eq, Show, Read, Ord)
-- only using special characters makes it an infix function 
-- we note the use of a syntatic construct
infixr 5 :-: 
data List' a = Emtpy | a :-: List' a
-- the fixity value tells us how tightly the operator binds, and if it is left and right associatiative 
-- we can do pattern matching similarly, i.e. (x :-: xs)

-- Defining a Tree
data Tree a = Empty' | Node a (Tree a) (Tree a) deriving (Show, Eq, Ord, Read)

singleTon :: a -> Tree a 
singleTon a = Node a Empty' Empty' 

treeInsert :: (Ord a) => a -> Tree a -> Tree a 
treeInsert x Empty' = singleTon x 
treeInsert x (Node head leftTree rightTree) 
    | x == head = Node head leftTree rightTree
    | x > head = Node head leftTree (treeInsert x rightTree)
    | x < head = Node head (treeInsert x leftTree) rightTree

-- we can define our own typeclass
-- for isntance, the Eq typeclass is defined as:
-- class Eq a where
    -- (==) :: a -> a -> Bool (THIS IS A FUNCTION DECLARATION - WE MUST INCLUDE THE TYPE DECLARATION)
    -- (/=) :: a -> a -> Bool
    -- x == y = not (x /= y) (This is not mandatory to add)
    -- x /= y = not (x == y)
class Eq' a where
    (===) :: a -> a -> Bool
    (/=/) :: a -> a -> Bool
    x === y = not (x /=/ y)
    x /=/ y = not (x === y)

-- here we defined the values in mutual recursion. This will be helpful when defining instances 
data TrafficLight = Green | Yellow | Red 
instance Eq' TrafficLight where 
    Red === Red = True
    Yellow === Yellow = True
    Green === Green = True
    _ === _ = False 
-- instance makes our type instances of typeclasses, much like how we did it with deriving
-- since === was defined in terms of /=/, we only have to overwrite one of them in the instance declaration 
instance Show TrafficLight where
    show Green = "GREEN"
    show Yellow = "YELLOW"
    show Red = "REDDD"

-- deriving instances by hand here gives us abit more control, enabling us to modify its behaviour 
-- we can also make typeclasses that are subclasses of other type classes 
-- class (Eq a) => Num a where ... 

-- we note 'a' has to be a concrete type in the creation of instances, not a type constructor. 
-- For deriving an instance of say "Maybe", we need to do: 
-- instance (Eq m) => Eq (Maybe m) where 
    -- Just x == Just y = x == y
    -- Nothing == Nothing = True
    -- _ == _ = False 
-- typeclass of m necessary as we are doing x == y
-- we need a concrete type in these cases because the typeclass definition requires a concrete type

-- :info typeclass in ghci will show the typclass instances
-- if we want to do something like [] meaning empty, we can something like 
class Yesno a where 
    yesno :: a -> Bool 

instance Yesno [a] where 
    yesno [] = False
    yesno _ = True

-- id is a function that takes a parameter and returns itself.

-- Functor typeclass is for things that can be mapped over 
-- class Functor f where
   -- fmap :: (a -> b) -> f a -> f b
-- here our typeclass does not use a concrete type, instead, it is a type constructor that takes a 
-- type parameter

-- instance Functor [] where
    -- fmap = map 

-- we note that types that require some sort of type parameter can be a functor, for instance, Maybe
-- instance Functor Maybe where
    -- fmap f (Just x) = Just (f x)
    -- fmap f Nothing = Nothing 

-- instance Functor (Either a) where
    -- fmap f (Right x) = Right (f x)
    -- fmap f (Left x) = Left x 

-- we dont rlly map the left, as then left and right need to be of the same type, and left is treated
-- to be the error message anyways

-- types have their own labels called kinds - a * means that the type is a concrete type 
-- :k Int -> Int :: *
-- :k Maybe -> Maybe :: * -> *
-- :k Maybe Int -> Maybe Int :: *




