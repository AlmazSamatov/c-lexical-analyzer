# C Lexical Analyzer
This analyzer was developed as a part of Compilers Construction course in University of Innopolis
## Getting Started
These instructions will help you run and test analyzer
### Prerequisites
* [Python3](https://www.python.org/downloads/)
* [Pytest](https://docs.pytest.org/en/latest/getting-started.html)
### Running the analyzer
Follow steps below to run the analyzer
1. Open folder where analyzer is located
2. Put your C code inside **in.c**
3. Open shell in current folder
4. Run ```python -m src.main``` or ```python3 -m src.main``` (if you have Python2 installed)
5. **TBD**
### Running the tests
If you have [created python venv](https://docs.python.org/3/library/venv.html) and installed Pytest in it:
1. [Activate venv](https://virtualenv.pypa.io/en/stable/userguide/) in shell
2. Go to folder where the analyzer is located via shell
3. Run ```python -m pytest test/``` or ```python3 -m pytest test/``` (if you have Python2 installed)

If you haven't installed python venv and using Pytest globally:
1. Go to folder where the analyzer is located via shell
2. Run ```python -m pytest test/``` or ```python3 -m pytest test/``` (if you have Python2 installed)
## Supported tokens
### Delimiters
Lexeme|Description|Program Representation|Integer Value
------|-----------|----------------------|-------------
[|Left Bracket|_LBRACKET|37
]|Right Bracket|_RBRACKET|38
(|Left Parentheses|_LP|39
)|Right Parentheses|_RP|40
{|Left Brace|_LBRACE|41
}|Right Brace|_RBRACE|42
' '|Space|_SPACE|43
/*|Left Multi Line commentary|_LCOM|44
*/|Right Multi Line commentary|_RCOM|45
//|Single Line commentary|_COM|46
'|Single Quote|_SQUOTE|47
"|Double Quote|_DQUOTE|48
;|Semicolon|_SEMI|85
### General Tokens
Lexeme|Description|Program Representation|Integer Value
------|-----------|----------------------|-------------
232sd*|Unknown lexeme|_ERROR|-1
723*|Integer number|_NUM|1
EOF*|End of file|_EOF|0
938.23*|Real number|_REAL|81
var*|Identifier|_IDENTIFIER|82
'd'*|Char|_CHAR|83
"random text"*|String|_STRING|84
* - and other possible variations in C
### Keywords
Lexeme|Description|Program Representation|Integer Value
------|-----------|----------------------|-------------
auto|Keyword auto|_AUTO|49
break|Keyword break|_BREAK|50
case|Keyword case|_CASE|51
char|Keyword char|_CHAR|52
const|Keyword const|_CONST|53
continue|Keyword continue|_CONTINUE|54
default|Keyword default|_DEFAULT|55
do|Keyword do|_DO|56
double|Keyword double|_DOUBLE|57
else|Keyword else|_ELSE|58
enum|Keyword enum|_ENUM|59
extern|Keyword extern|_EXTERN|60
float|Keyword float|_FLOAT|61
for|Keyword for|_FOR|62
goto|Keyword goto|_GOTO|63
if|Keyword if|_IF|64
int|Keyword int|_INT|65
long|Keyword long|_LONG|66
register|Keyword register|_REGISTER|67
return|Keyword return|_RETURN|68
short|Keyword short|_SHORT|69
signed|Keyword signed|_SIGNED|70
static|Keyword static|_STATIC|71
struct|Keyword struct|_STRUCT|72
switch|Keyword switch|_SWITCH|73
typedef|Keyword typedef|_TYPEDEF|74
union|Keyword union|_UNION|75
unsigned|Keyword unsigned|_UNSIGNED|76
void|Keyword void|_VOID|77
volatile|Keyword volatile|_VOLATILE|78
while|Keyword while|_WHILE|79
### Operators
Lexeme|Description|Program Representation|Integer Value
------|-----------|----------------------|-------------
+|Plus|_PLUS|2
-|Minus|_MINUS|3
*|Star|_STAR|4
/|Division|_DIV|5
%|Modulo operation|_MOD|6
=|Assignment|_ASSIGN|7
+=|Plus and assignment|_PASSIGN|8
-=|Minus and assignment|_MASSIGN|9
*=|Multiplication and assignment|_MULASSIGN|10
/=|Division and assignemnt|_DIVASSIGN|11
%=|Modulo operation and assignment|_MODASSIGN|12
==|Equality|_EQ|13
\>|Greater than|_GT|14
\<|Less than|_LT|15
!=|Not equal|_NEQ|16
\>=|Greater or equal|_GTEQ|17
\<=|Less or equal|_LTEQ|18
&&|Logical AND|_LAND|19
\|\||Logical OR|_LOR|20
!|Logical NOT|_LNOT|21
&|Bitwise AND|_AND|22
\||Bitwise OR|_BOR|23
^|Bitwise XOR|_BXOR|24
~|Bitwise complementary|_BCOMP|25
\<\<|Bitwise left shift|_LSHIFT|26
\>\>|Bitwise right shift|_RSHIFT|27
sizeof|sizeof operator|_SIZEOF|28
&=|Bitwise AND and assignemnt|_BANDASSIGN|29
\|=|Bitwise OR and assignment|_BORASSIGN|30
^=|Bitwise XOR and assignment|_BXORASSIGN|31
<<=|Bitwise left shit and assignment|_LSHIFTASSIGN|32
\>\>=|Bitwise right shift and assignment|_RSHIFTASSIGN|33
,|Comma|_COMMA|34
?|Question mark|_QUEST|35
:|Colon|_COLON|36
->|Selection operator|_SELECT|86
## Authors
* [**Asapov Timur**](https://github.com/Myyyth) - 3rd year student of Innopolis University
* [**Samatov Almaz**](https://github.com/AlmazSamatov) - 3rd year student of Innopolis University
## References
* [https://www.programiz.com/c-programming/c-operators](https://www.programiz.com/c-programming/c-operators)
* [https://www.cs.auckland.ac.nz/references/unix/digital/AQTLTBTE/DOCU_059.HTM](https://www.cs.auckland.ac.nz/references/unix/digital/AQTLTBTE/DOCU_059.HTM)
