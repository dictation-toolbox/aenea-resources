====================
tComment
====================

Operators::

    gc{motion}   :: Toggle comments
    gc<Count>c{motion} :: Toggle comment text with count 
    gcc          :: Toggle comment for the current line
    gC{motion}   :: Comment region
    gCc          :: Comment the current line

In visual mode::

    gc           :: Toggle comments
    gC           :: Comment selected text

Primary key maps for normal and insert mode::

    <c-_><c-_>   :: :TComment
    <c-_><space> :: :TComment <QUERY COMMENT-BEGIN ?COMMENT-END>
    <c-_>b       :: :TCommentBlock
    <c-_>a       :: :TCommentAs <QUERY COMMENT TYPE>
    <c-_>n       :: :TCommentAs &filetype <QUERY COUNT>
    <c-_>s       :: :TCommentAs &filetype_<QUERY COMMENT SUBTYPE>
    <c-_>i       :: :TCommentInline
    <c-_>r       :: :TCommentRight
    <c-_>p       :: Comment the current inner paragraph
    <c-_><Count> :: :TComment with count argument (a number from 1 to 9)

Primary key maps for visual mode::

    <c-_><c-_>   :: :TComment
    <c-_>i       :: :TCommentInline
    <c-_><Count> :: :TComment with count argument (a number from 1 to 9)

A secondary set of key maps is defined for normal and insert mode::

    <Leader>__       :: :TComment
    <Leader>_p       :: Comment the current inner paragraph
    <Leader>_<space> :: :TComment <QUERY COMMENT-BEGIN ?COMMENT-END>
    <Leader>_i       :: :TCommentInline
    <Leader>_r       :: :TCommentRight
    <Leader>_b       :: :TCommentBlock
    <Leader>_a       :: :TCommentAs <QUERY COMMENT TYPE>
    <Leader>_n       :: :TCommentAs &filetype <QUERY COUNT>
    <Leader>_s       :: :TCommentAs &filetype_<QUERY COMMENT SUBTYPE>

... and for select mode::

    <Leader>__       :: :TComment
    <Leader>_i       :: :TCommentInline
