# congrlang
Congruence Language (or "CongrLang" for short) is a constructed language where all words, and inflections are natural numbers and the morphology is based on modulo arithmetic. The inflections are rendered as sequences of readable syllables by versions.
## Conception
This constructed language is based on the idea of a language where the morphology is so complex that it is considered completely irregular.
## Morphology
The inflection of a word is the least natural number congruent to the power of the primitive form of the word. The methodology accords with the following expression:
```
m=a**b%p
```
where
* `m` is the inflection of the word `a`, the primitive state.
* `b` denotes the inflection the word has.
* `p` represents the designated substantial prime number.
## Syntax
The syntax implements the Chinese Remainder Theorem. Each item is assigned a moderately big prime, and then merge the items into a product, supposing that it remains each inflection when divided by the product of all the primes.
