import Control.Applicative (Alternative(empty))
-- functions names cant start with capitalised letters ( for data constructors )
doubleMe x = x + x
doubleUs x y = x*2 + y*2

doubleSmallNumber x = if x < 10
                        then x *2
                        else x
-- If-Else statements require the else statement

doubleSmallNumber' x  = (if x < 10 then x*2 else x) + 1
-- ' to indicate strict versions of functions 

-- !! to extract element from list
-- list must be all of the same type
-- when comparing list they compare from the first to the last elements 
-- head, tail, last, init for list - head returns first and tail returns the rest, vice versa
-- length, null, reverse, take int list (extract first int from list), drop (return not taken from take)
-- minimum, maximum for list, sum, product, elem: test for existance 

-- cycle [] for infinite list of list provided, repeat _ for one element

-- [x | x <- [50..100], mod x 7 == 3] list of no between 50 and 100 with x = 3 mod 7

boomBang xs = [if x < 10 then "BANG" else "Boom" | x <- xs, odd x]

-- [x | x <- [10..20], x /= 13, x /= 15, x /= 19]
-- [x * y | x <- [2, 5, 10], y <- [5, 9, 10] ]

length' xs = sum [1 | _ <- xs] -- use  _ if we wont use the variable

removeUpperCase :: [Char] -> [Char]
removeUpperCase xs = [c | c <- xs, c `elem` ['a'..'z']]
-- we can also do its logical inverse 
removeUpperCase' xs = [c | c <- xs, (not) (c `elem` ['A'..'Z'])] -- alternative 'notElem'

-- let xxs = [[1,3,5,2,3,1,2,4,5],[1,2,3,4,5,6,7,8,9],[1,2,4,2,1,6,3,1,3,2,3,6]]
-- ghci> [[x | x <- xs, even x] | xs <- xxs] Remove odd number from the list in list

-- tuples given by  (), can be any size + components do not need to be homogenous - note that
-- each different tuple is of a different type + size is fixed
-- fst, snd for pairs

zip' xs ys = [(xs !! x, ys !! x) | x <- [0..(min (length xs) (length ys)  - 1)]]

-- [(x, y, z) | x <- [1..10], y <- [1..x], z <- [1..y], x^2 == y^2 + z^2, x + y + z == 24 ]  
-- find all right angle triangles with sides < 10 and perimeter 24

-- TYPES: 
-- some types: Int (bounded by 2^31 below and above), Integer (int but unbounded)
-- float, double w 2x the pricision
-- bool
-- Char denoted by '', string ""


-- TYPECLASS: 
-- Eq, for equality 
-- Ord, for ordering - types must be part of Eq
-- Show, for presenting as string - function "show" converts from some type to string
-- Read, for reading a string - function "read" converts from string to some type
    -- note read must be used in some context - either use it in a function, or set a type with ::
    -- read "True" || False  and read "5" :: Int
-- Enum, with successors and predecesors 
-- Bounded , for uipper and lower bound
-- Num, for numbers - Int, Float etc lie in this class 
-- Integral, for WHOLE numbers - only Int and Integer
-- Floating, for floating point - only Float and Double 
-- Note "fromIntegral" Function - takes integral and changes to smth in Num 

lucky :: (Integral a) => a -> String
lucky 7 = "Success!"
lucky x = "UNLUCKY"

inbetween :: (Integral a) => a -> String
inbetween 1 = "ONE"
inbetween 2 = "TWO"
inbetween x = "OUTSIDE"

factorial' :: (Integral a) => a -> a
factorial' 0 = 1
factorial' x = x * factorial' (x-1)

addVectors :: (Num a) => (a, a) -> (a, a) -> (a, a)
addVectors (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

first :: (a, b , c) -> a
first (x, _, _) = x

-- pattern matching works in list comprehension 
-- [a + b | (a, b) <- xs], xs = [(1,3), (4,3), (2,4), (5,3), (5,6), (3,1)]

head' :: [a] -> a
head' [] = error "EMPTY" -- note error function
head' (x:_) = x -- note that the pattern must be in parentheses

length'' :: (Num b) => [a] -> b
length'' [] = 0
length'' (_:xs) = 1 + length'' xs

sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs
-- omitting the classtype will result in an error, because haskell looks at 0 and + and knows this
-- has to be part of the num class, so it will complain that you havent added that in
-- https://stackoverflow.com/questions/49877023/no-instance-for-num-a-arising-from-a-use-of-haskell 

firstLetter :: String -> String
firstLetter all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]
-- note if we use a string in input, it must be surrounded with "", even in CLI

-- For inputs of different formats, we use pattern matching
-- For the same input format, we can check it differently w guards and if-then-else statements

bmiTell :: (RealFloat a) => a -> String
bmiTell bmi
    | bmi <= 18.5 = "UNDERWEIGHT!!"
    | bmi <= 25 = "OK!"
    | otherwise = "FATTT"

max' :: (Ord a) => a -> a -> a
max' a b | a > b = a | otherwise = b

bmiTell' :: (RealFloat a) => a -> a -> String
bmiTell' weight height
    | bmi <= skinny = "UNDERWEIGHT!!"
    | bmi <= normal = "OK!"
    | otherwise = "FATTT"
    where bmi = weight / (height^2)
          (skinny, normal) = (18.5, 25)

initials :: String -> String -> String
initials firstName lastName = [f,l]
    where (f:_) = firstName
          (l:_) = lastName

calcBmi :: (RealFloat a) => [(a, a)] -> [a]
calcBmi xs = [bmi w h | (w, h) <- xs]
    where bmi height weight = height / weight^2

-- Where bindings are a syntactic construct that let you bind to variables at the end of a function 
-- and the whole function can see them, including all the guards. Let bindings let you bind to 
-- variables anywhere and are expressions themselves, but are very local, so they don't span across 
-- guards.
volume :: (RealFloat a) => a -> a -> a
volume r h =
    let sideArea = 2 * pi *r * h
        topArea = pi * (r^2)
    in sideArea + 2*topArea

-- 4 * (let a = 9 in a + 1) + 2 is a valid express'ion 
-- [let square x = x^2 in (square 3, square 4, square 5)] is also valid
-- (let (a,b,c) = (1,2,3) in a+b+c) * 10
calcBmi' :: (RealFloat a) => [(a, a)] -> [a]
calcBmi' xs = [bmi | (w, h) <- xs, let bmi = w / h ^ 2]

-- The names defined in a let inside a list comprehension are visible to the output function (the part 
-- before the |) and all predicates and sections that come after of the binding.
-- We omitted the in part of the let binding when we used them in list comprehensions because the 
-- visibility of the names is already predefined there. However, we could use a let in binding in a 
-- predicate and the names defined would only be visible to that predicate.

-- alternative for pattern matching on parameters is synthetic sugar for case expressions. 
-- can be used as: 
describeList :: [a] -> String
describeList xs = "The List is " ++ case xs of [] -> "empty"
                                               [x] -> "single"
                                               xs -> "long"

describeList' :: [a] -> String
describeList' xs = "The list is " ++ what xs
    where what [] = "empty"
          what [x] = "single"
          what xs = "long"

maximum' :: (Ord a) => [a] -> a
maximum' [] = error "HELP"
maximum' [x] = x
maximum' (x:xs)
    | x > maxTail = x
    | otherwise = maxTail
    where maxTail = maximum' xs
-- OR maximum' (x:xs) = max x (maximum' xs)

replicate' :: (Num a, Ord a) => a -> b -> [b]
replicate' n x
    | n <= 0 = []
    | otherwise = x:replicate' (n-1) x

take'' :: (Num a, Ord a) => a -> [b] -> [b]
take'' n all@(x:xs)
    | n <= 0 = []
    | null (x:xs) = [] -- THIS DOSENT WORK because we cant match x:xs against []
    | otherwise = x:take'' (n-1) xs

take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
    | n <= 0   = []
take' _ []     = []
take' n (x:xs) = x : take' (n-1) xs

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse xs ++ [x]

repeat' :: a -> [a]
repeat' x = x:repeat' x

zip'' :: [a] -> [b] -> [(a,b)]
zip'' [] _ = []
zip'' _ [] = []
zip'' (x:xs) (y:ys) = (x,y):zip'' xs ys

elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False
elem' toFind (x:xs)
    | toFind == x = True
    | otherwise = elem' toFind xs

quicksort' :: (Ord a) => [a] -> [a]
quicksort' [] = []
quicksort' (x:xs) = 
    let smaller = [a | a <- xs, a <= x]
        larger = [a | a <- xs, a > x]
    in quicksort' smaller ++ [x] ++ quicksort' larger

-- Currying functions 
multThree :: (Num a) => a -> a -> a -> a
multThree x y z = x * y * z 
-- we can do: let MultTwowithNine = multThree 9
-- we can do: let MultOneithEighteen = multThree 9 2

comparewithHundred :: (Num a, Ord a) => a -> Ordering
comparewithHundred = compare 100 

dividebyTen :: (Floating a) => a -> a 
dividebyTen = (/10)

-- we can pass functions as input to other functions
applyTwice :: (a -> a) -> a -> a 
applyTwice f x = f (f x) 
-- this allows us to do things like: applyTwice (+1000) 5 and applyTwice (3:) [1] -> [3, 3, 1]

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ _ [] = []
zipWith' _ [] _ = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys
-- note if we want to use an infix function we need to wrap it in parentheses. 

flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f = g
    where g x y = f y x

-- technically because of currying and partially applied functions, we can really just define it as
flip'' :: (a -> b -> c) -> b -> a -> c
flip'' f y x = f x y

map' :: (a -> b) -> [a] -> [b]
map' _ [] = []
map' f (x:xs) = f x: map' f xs 

-- filter is a function that takes a predicate (a predicate is a function that tells whether 
-- something is true or not, so in our case, a function that returns a boolean value) and a list 
-- and then returns the list of elements that satisfy the predicate

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' f (x:xs)
    | f x = x : filter' f xs 
    | otherwise = filter' f xs 

quicksort'' :: (Ord a) => [a] -> [a]
quicksort'' [] = []
quicksort'' (x:xs) = 
    let smallSorted = quicksort'' (filter' (<=x) xs)
        largeSorted = quicksort'' (filter' (>x) xs)
    in smallSorted ++ [x] ++ largeSorted

largestDivisible :: (Integral a) => a 
largestDivisible = head (filter p [10000, 9999..])
    where p x = mod x 3829 == 0

-- sum of all odd squares smaller than 10000
-- sum (takeWhile (<10000) (map (^2) [1, 3..]))
-- It takes a predicate and a list and then goes from the beginning of the list and 
-- returns its elements while the predicate holds true
-- sum (takeWhile (<10000) [a | x <- [1..], let a = x^2, odd a])

-- find Collatz squence of length > 15 for starting no 1 - 100
collatz :: (Integral a) => a -> [a]
collatz 1 = [1]
collatz n 
    | odd n = n: collatz (3 * n + 1)
    | otherwise = n: collatz (div n 2)

-- we have 2 numbers, first is the starting number, second is the length to compare against
collatzLength :: (Integral a) => a -> a -> a
collatzLength x _ 
    | x < 0 = 0
collatzLength 1 n 
    | length (collatz 1) >= n = 1
    | otherwise = 0
collatzLength x n 
    | length (collatz x) >= n = 1 + collatzLength (x-1) n 
    | otherwise = collatzLength (x-1) n 

