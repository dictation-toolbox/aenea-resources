====================
Verbal Emacs
====================

Motions::

    "up":Text("k"),
    "down":Text("j"),
    "left":Text("h"),
    "right":Text("l"),

    "lope":Text("b"),
    "yope":Text("w"),
    "elope":Text("ge"),
    "iyope":Text("e"),

    "lopert":Text("B"),
    "yopert":Text("W"),
    "elopert":Text("gE"),
    "eyopert":Text("E"),

    "apla":Text("{"),
    "anla":Text("}"),
    "sapla":Text("("),
    "sanla":Text(")"),

    "care":Text("^"),
    "hard care":Text("0"),
    "doll":Text("$"),

    "screecare":Text("g^"),
    "screedoll":Text("g$"),

    "scree up":Text("gk"),
    "scree down":Text("gj"),

    "wynac":Text("G"),

    "wynac top":Text("H"),
    "wynac toe":Text("L"),

    "[inner | outer]
       [lope | yope][ert]":"daw/diw"

    "tect":Text("%%"),
    "matu":Text("M"),

    "phytic":"f",
    "fitton":"F",
    "pre phytic":"t",
    "pre fitton":"T",

    # CamelCaseMotion plugin
    "calalope":Text(",b"),
    "calayope":Text(",w"),
    "end calayope":Text(",e"),
    "inner calalope":Text("i,b"),
    "inner calayope":Text("i,w"),
    "inner end calayope":Text("i,e"),

    # EasyMotion
    "easy [lope | yope |
           elope | iyope][ert]",

Commands::

    "vim scratch":Key("X"),
    "vim chuck":Key("x"),
    "vim undo":Key("u"),
    "plap":Key("P"),
    "plop":Key("p"),
    "ditto":Text("."),
    "ripple":macro
    "rec ripple <nato>":record macro
    "end ripple":stop recording macro
  spec = "[<count>] [reg <nato>] <cmd>"

Operators::

    "relo":"",
    "dell":"d",
    "chaos":"c",
    "nab":"y",
    "swap case":"g~",
    "uppercase":"gU",
    "lowercase":"gu",
    "external filter":"!",
    "external format":"=",
    "format text":"gq",
    "rotate thirteen":"g?",
    "indent left":"<",
    "indent right":">",
    "define fold":"zf",
    "comm nop":"gcc",

Insertions::

  Any insertion: parrot N

  #  Keys
    "ace [<count>]":        Key("space:%(n)d"),
    "tab [<count>]":        Key("Tab:%(n)d"),
    "slap [<count>]":       Key("Return:%(n)d"),
    "chuck [<count>]":      Key("Delete:%(n)d"),
    "scratch [<count>]":    Key("BackSpace:%(n)d"),
    "ack":                  Key("Escape"),

    # Symbols
    "amp":        Key("ampersand"),
    "star":       Key("asterisk"),
    "at sign":    Key("at"),
    "back ash":   Key("backslash"),
    "backtick":   Key("grave"),
    "bar":        Key("bar"),
    "hat":        Key("asciicircum"),
    "yeah":       Key("colon"),
    "drip":       Key("comma"),
    "dollar":     Key("dollar"),
    "dot":        Key("period"),
    "quote":      Key("quotedbl"),
    "eek":        Key("equal"),
    "bang":       Key("exclam"),
    "pound":      Key("numbersign"),
    "hyph":       Key("minus"),
    "percent":    Key("percent"),
    "cross":      Key("plus"),
    "quest":      Key("question"),
    "ash":        Key("slash"),
    "smote":      Key("apostrophe"),
    "tilde":      Key("asciitilde"),
    "rail":       Key("underscore"),
    "push":       Key("parenleft"),
    "pop":        Key("parenright"),

    # Nested
    "circle":           Nested("()"),
    "square":           Nested("[]"),
    "box":              Nested("[]"),
    "diamond":          Nested("<>"),
    "hexy":             Nested("{}"),
    "nest quote":       Nested("\"\""),
    "nest smote":       Nested("''"),

    # Spelling
    "alpha bravo etc..."
    "dig 0, dig5, etc..."

    # Python
    "private":          Nested("____"),
    "dub dock string":  Nested('""""""'),
    "dock string":      Nested("''''''"),
    "values":           Text("values"),
    "get atter":        Text("getattr"),
    "set atter":        Text("setattr"),
    "has atter":        Text("hasattr"),
    "print":            Text("print"),
    "if test":          Text("if "),
    "elif":             Text("elif "),
    "else":             Text("else"),
    "deaf":             Text("def "),
    "log and":          Text("and "),
    "log or":           Text("or "),
    "log not":          Text("not "),
    "not":              Text("not "),
    "for loop":         Text("for "),
    "bit ore":          Text("| "),
    "bit and":          Text("& "),
    "bit ex or":        Text("^ "),
    "times":            Text("* "),
    "divided":          Text("/ "),
    "plus":             Text("+ "),
    "minus":            Text("- "),
    "plus equal":       Text("+= "),
    "minus equal":      Text("-= "),
    "times equal":      Text("*= "),
    "divided equal":    Text("/= "),
    "mod equal":        Text("%%= "),
    "as name":          Text("as "),
    "in":               Text("in "),
    "is":               Text("is "),
    "while":            Text("while "),
    "class":            Text("class "),
    "with context":     Text("with "),
    "import":           Text("import "),
    "raise":            Text("raise "),
    "return":           Text("return "),
    "none":             Text("None"),
    "try":              Text("try"),
    "except":           Text("except"),
    "lambda":           Text("lambda "),
    "assert":           Text("assert "),
    "delete":           Text("del "),
    "assign":           Text("= "),
    "compare eek":      Text("== "),
    "compare not eek":  Text("!= "),
    "compare greater":  Text("> "),
    "compare less":     Text("< "),
    "compare geck":     Text(">= "),
    "compare lack":     Text("<= "),

Identifiers::

    ("[literal] [upper | natural]"
       "( proper | camel | rel-path | abs-path |"
       "  score | scope-resolve | jumble |"
       "  dotword | dashword | natword |"
       "  snakeword | brooding-narrative)"
     "[<dictation>]")
