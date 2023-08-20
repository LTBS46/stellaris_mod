// DELETE THIS CONTENT IF YOU PUT COMBINED GRAMMAR IN Parser TAB
lexer grammar StellarisLexer;

TREE_TYPE : 'tree_' ([a-zA-Z_]+ '_')? [_0-9]*[0-9] ;
LANGUAGE : 'l_' [a-zA-Z_][a-zA-Z_]* ;

ADMIRAL : 'admiral' ;               // keyword
ADOPT : 'adopt' ;                   // keyword
AI : 'ai' ;                         // keyword
ALL : 'all' ;                       // keyword
ANCIENT : 'ancient' ;               // dlcname
ANY : 'any' ;                       // keyword
APOCALYPSE : 'apocalypse' ;         // dlcname
ASCENSION : 'ascension' ;           // keyword
BALANCE : 'balance' ;               // mod_cat, keyword
BUILDINGS : 'buildings' ;           // mod_cat
CADET : 'cadet' ;                   // keyword
CAPACITY : 'capacity' ;             // keyword
CAPTAIN : 'captain' ;               // keyword
CARAVANEERS : 'caravaneers' ;       // keyword
CATEGORY : 'category' ;             // keyword
CIVIC : 'civic' ;                   // keyword
CIVILIAN : 'civilian' ;             // keyword
CLIENT : 'client' ;                 // keyword
COMMAND : 'command' ;               // keyword
COMMODORE : 'commodore' ;           // keyword
COUNTRY : 'country' ;               // keyword
COUNT : 'count' ;                   // keyword
DAWN : 'dawn' ;                     // dlcname
DAYS : 'days' ;                     // keyword
DANGEROUS : 'dangerous' ;           // keyword
DEFAULT : 'default' ;               // keyword
DESC : 'desc' ;                     // keyword
DIFFICULTY : 'difficulty' ;         // keyword
DIPLOMACY : 'diplomacy' ;           // mod_cat
DISABLED : 'disabled' ;             // keyword
DLC : 'dlc' ;                       // keyword
ECONOMY : 'economy' ;               // mod_cat
ENABLED : 'enabled' ;               // keyword
ENGINEERING : 'engineering' ;       // keyword
ENSIGN : 'ensign' ;                 // keyword
EVENT : 'event' ;                   // keyword
EVENTS : 'events' ;                 // mod_cat
FALSE : 'false' ;                   // boolean
FEDERATIONS : 'federations' ;       // dlcname
FINISH : 'finish' ;                 // keyword
FIXES : 'fixes' ;                   // mod_cat
GAMEPLAY : 'gameplay' ;             // mod_cat
GRAND : 'grand' ;                   // keyword
GRAPHICS : 'graphics' ;             // mod_cat
HAS : 'has' ;                       // keyword
HOST : 'host' ;                     // keyword
IRONMAN : 'ironman' ;               // keyword
IS : 'is' ;                         // keyword
LABEL : 'label' ;                   // keyword
LIMIT : 'limit' ;                   // keyword
LOCALE : 'locale' ;                 // keyword
MEGASTRUCTURES : 'megastructures' ; // mod_cat
MOD : 'mod' ;                       // keyword
NAVAL : 'naval' ;                   // keyword
NEMESIS : 'nemesis' ;               // dlcname
ORIGIN : 'origin' ;                 // keyword
OVERHAUL : 'overhaul' ;             // mod_cat
OVERLORD : 'overlord' ;             // dlcname
PACK : 'pack' ;                     // dlcname
PARAGON : 'paragon' ;               // dlcname
PASSED : 'passed' ;                 // keyword
PERK : 'perk' ;                     // keyword
PHYSICS : 'physics' ;               // keyword
RARE : 'rare' ;                     // keyword
RELICS : 'relics' ;                 // dlcname
SOCIETY : 'society' ;               // keyword
STORY : 'story' ;                   // dlcname
SYNTHETHIC : 'synthethic' ;         // dlcname
SWITCH : 'switch' ;                 // keyword
TECHNOLOGIES : 'technologies' ;     // mod_cat
TECHNOLOGY : 'technology' ;         // keyword
TAGS : 'tags' ;                     // keyword
TRADITION : 'tradition' ;           // keyword
TRUE : 'true' ;                     // boolean
UTILITIES : 'utilities' ;           // mod_cat
UTOPIA : 'utopia' ;                 // dlcname
VALID : 'valid' ;                   // keyword
VAR : 'var' ;                       // keyword
VERSION : 'version' ;               // keyword
VISIBLE : 'visible' ;               // keyword
WEIGHT : 'weight' ;                 // keyword

OR : 'or' | '||' | '|' ;
AND : 'and' | '&&' | '&' ;
XOR : 'xor' | '^^' | '^' ;
NOT : 'not' | '!' ;

OPLESS : '>' ;
OPMORE : '<' ;
LEQ : '<=' ;
MEQ : '>=' ;
NEQ : '!=' ;
DEQ : '==' ;

EQ : '=' ;
STAR : '*' ;


COMMA : ',' ;
SEMI : ';' ;
COLON : ':' ;
DOT : '.' ;
AT : '@' ;

LPAREN : '(' ;
RPAREN : ')' ;
LSQUAR : '[' ;
RSQUAR : ']' ;
LCURLY : '{' ;
RCURLY : '}' ;

INT : [0-9]+ ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
STRING: '"' ('\\' ["\\] | ~["\\\r\n])* '"' ;
WS: [ \t\n\r\f]+ -> skip ;

fragment A : 'a' | 'A' ;