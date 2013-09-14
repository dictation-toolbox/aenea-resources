==============================
Fugitive
==============================

"git status"
:Gstatus                Bring up the output of git-status in the preview window.  The following maps, which work on the cursor line file where sensible, are provided:::

                        <C-N> next file
                        <C-P> previous file
                        <CR>  :Gedit
                        -     :Git add
                        -     :Git reset (staged files)
                        cA    :Gcommit --amend --reuse-message=HEAD
                        ca    :Gcommit --amend
                        cc    :Gcommit
                        cva   :Gcommit --amend --verbose
                        cvc   :Gcommit --verbose
                        D     :Gdiff
                        ds    :Gsdiff
                        dp    :Git! diff (p for patch; use :Gw to apply)
                        dp    :Git add --intent-to-add (untracked files)
                        dv    :Gvdiff
                        O     :Gtabedit
                        o     :Gsplit
                        p     :Git add --patch
                        p     :Git reset --patch (staged files)
                        q     close status
                        R     reload status
                        S     :Gvsplit

"git commit"
:Gcommit [args]         A wrapper around git-commit.  If there is nothing to commit, :Gstatus is called instead.  Unless the arguments given would skip the invocation of an editor (e.g., -m), a split window will be used to obtain a commit message.  Write and close that window (:wq or :Gwrite) to finish the commit.  Unlike when running the actual git-commit command, it is possible (but unadvisable) to muck with the index with commands like git-add and git-reset while a commit message is pending.

"git diff"
:Gdiff [revision]       Perform a vimdiff against the current file in the given revision.  With no argument, the version in the index is used (which means a three-way diff during a merge conflict, making it a git-mergetool alternative).  The newer of the two files is placed to the right.  Use do and dp and write to the index file to simulate "git add --patch".

"git move"
:Gmove {destination}    Wrapper around git-mv that renames the buffer afterward.  The destination is relative to the current directory except when started with a /, in which case it is relative to the work tree.  Add a ! to pass -f.

"git remove"
:Gremove                Wrapper around git-rm that deletes the buffer afterward.  When invoked in an index file, --cached is passed.  Add a ! to pass -f and forcefully discard the buffer.

