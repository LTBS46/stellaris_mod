parser grammar StellarisParser;
options { tokenVocab=StellarisLexer; }

mod:
    descriptor
    content*
    ;
    
descriptor:
    MOD mod_name=ID LCURLY
        mod_version?
        game_version?
        tags
    RCURLY
    ;

game_version:
    VERSION EQ version_value
    ;

mod_version:
    MOD VERSION EQ version_value
    ; 

version_value:  STAR
    | INT (
        DOT (STAR | (INT (
            DOT (STAR | INT)
        )?))
    )?;

tags:
    TAGS EQ LSQUAR
        tag (COMMA tag)*
    RSQUAR
    ;

tag:    BALANCE
    |   BUILDINGS
    |   DIPLOMACY
    |   ECONOMY
    |   EVENTS
    |   FIXES
    |   GAMEPLAY
    |   GRAPHICS
    |   MEGASTRUCTURES
    |   OVERHAUL
    |   TECHNOLOGIES
    |   UTILITIES
    ;
    

content:tradition_category
    |   civic
    |   origin
    |   country_event
    |   event
    |   aperk
    |   technology


    |   label
    |   variable
    ;

variable: VAR name=ID ;

technology:
    TECHNOLOGY name=ID COLON field=(ENGINEERING|PHYSICS|SOCIETY)
    (COMMA (RARE | DANGEROUS))?
    LCURLY
    CATEGORY EQ ID
    description?
    RCURLY
    ;

label:
    LABEL name=ID EQ label_any_language
    ;
    
aperk:
    ASCENSION PERK name=ID LCURLY
    description?
    RCURLY
    ;
    
country_event:
    COUNTRY EVENT name=ID LCURLY RCURLY
    ;
    
event:
    EVENT name=ID LCURLY RCURLY
    ;

tradition_category:
    TRADITION CATEGORY name=ID COLON tree=TREE_TYPE
    LCURLY
    description?
    valid_empire?
    visible_empire?
    ADOPT EQ (ta=tradition_item | adopt_id=ID)
    TRADITION EQ LSQUAR
        (t1=tradition_item | n1=ID)
        (t2=tradition_item | n2=ID)
        (t3=tradition_item | n3=ID)
        (t4=tradition_item | n4=ID)
        (t5=tradition_item | n5=ID)
    RSQUAR
    FINISH EQ (tf=tradition_item | finish_id=ID)
    RCURLY
    ;

tradition_item:
    TRADITION name=ID LCURLY
    description?  
    RCURLY;

valid_empire:
    VALID EQ bool_expr_empire_or
    ;

bool_expr_empire_or:
    bool_expr_empire_and (OR bool_expr_empire_or)?
    ;

bool_expr_empire_and:
    bool_expr_empire_xor (AND bool_expr_empire_and)?
    ;

bool_expr_empire_xor:
    bool_expr_empire_val (XOR bool_expr_empire_xor)?
    ;

bool_expr_empire_val:
    TRUE | FALSE | LPAREN bool_expr_empire_or RPAREN
    | NOT bool_expr_empire_or | bool_expr_any_val
    | ALL LPAREN (bool_expr_empire_or (COMMA bool_expr_empire_or)*) RPAREN
    | ANY LPAREN (bool_expr_empire_or (COMMA bool_expr_empire_or)*) RPAREN
    | BALANCE rel_syms INT
    | CIVIC COUNT? rel_syms INT
    | COMMAND LIMIT? rel_syms INT
    | NAVAL CAPACITY? rel_syms INT
    ;

bool_expr_any_val:
    |   HAS? (CLIENT | HOST)? DLC (dlc_names|LPAREN dlc_names (COMMA dlc_names)* RPAREN)
    |   IS? DIFFICULTY rel_syms (INT | difficulty_name)
    |   CARAVANEERS (ENABLED | DISABLED|)
    |   DAYS PASSED? rel_syms INT
    |   IS? IRONMAN

    ;
    
difficulty_name: CIVILIAN | CADET | ENSIGN | CAPTAIN | COMMODORE | GRAND? ADMIRAL ;

rel_syms: NEQ | DEQ | OPMORE | OPLESS | MEQ | LEQ ;

visible_empire:
    VISIBLE EQ bool_expr_empire_and
    ;

civic:
    CIVIC ID
    LCURLY
    (description?)
    RCURLY
    ;
    
origin:
    ORIGIN ID
    LCURLY
    (description?)
    RCURLY
    ;

dlc_names:  UTOPIA
    |       SYNTHETHIC DAWN
    |       APOCALYPSE
    |       OVERLORD
    |       NEMESIS
    |       PARAGON
    |       ANCIENT RELICS STORY PACK
    |       FEDERATIONS
    ;

description:
    DESC EQ label_any_language
    ;
    
label_any_language: ID
    |               STRING
    |               SWITCH LPAREN LOCALE RPAREN LCURLY
                    lal_content
                    RCURLY
    ;
    
lal_content:    (LANGUAGE COLON label_language)+
    |           (LANGUAGE COLON label_language)*
                DEFAULT COLON label_language
    ;
    
label_language: ID
    |           STRING
    ;