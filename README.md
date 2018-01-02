# web-ceasar
## Need to correct original file, see requirements for correction
### The initial value of the text input field should was 0
### The rotation amount of 0 preserves the original phrase.
### Text rotated input text by 13, then rotated the resulting text by 13 and went back the original text.
### Some rotation amount other than 13 did not work.
## Cause of problem: mis-named caesar file
### Upon correction, passed all tests as outlined below:
#### Submitting the form with a rotation integer and message results in the encrypted text being displayed. For example, rotating "The crow flies at midnight!" by 13 gives "Gur pebj syvrf ng zvqavtug!".
#### Rotation preserves spaces and punctuation.
#### Successively rotating by complementary amounts--e.g. 13 and 13, 10 and 16, 4 and 22, etc.--gives the same message that you started with.


