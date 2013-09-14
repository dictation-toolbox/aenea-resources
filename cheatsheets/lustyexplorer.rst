=========================
Lusty Explorer
=========================
Usage:::

                 <Leader>lf  - files
                 <Leader>lr  - cur file dir
                 <Leader>lb  - buffers
                 <Leader>lg  - buffer grep
                 "rusty [absolute] [name]" - open files

You can also use the commands:::

                 ":LustyFilesystemExplorer [optional-path]"
                 ":LustyFilesystemExplorerFromHere"
                 ":LustyBufferExplorer"
                 ":LustyBufferGrep"

As you type, the table updates for possible matches using a
fuzzy matching algorithm (or regex matching, in the case of
grep).  Special keys include:::

                 <Enter>  open selected match
                 <Tab>    open selected match
                 <Esc>    cancel
                 <C-c>    cancel
                 <C-g>    cancel

                 <C-t>    open selected match in a new [t]ab
                 <C-o>    open selected match in a new h[o]rizontal split
                 <C-v>    open selected match in a new [v]ertical split

                 <C-n>    select [n]ext match
                 <C-p>    select [p]revious match
                 <C-f>    select [f]orward one column
                 <C-b>    select [b]ack one column

                 <C-u>    clear prompt

               Additional shortcuts for the filesystem explorer:

                 <C-w>    ascend one directory at prompt
                 <C-r>    [r]efresh directory contents
                 <C-a>    open [a]ll files in current table
                 <C-e>    create new buffer with the given name and path

