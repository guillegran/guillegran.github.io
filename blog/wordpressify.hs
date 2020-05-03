#!/usr/bin/env runhaskell
-- wordpressify.hs
import Text.Pandoc.JSON

main = toJSONFilter wordpressify
  where wordpressify (Math x y) = Math x ("LaTeX " ++ y)
        wordpressify x = x
