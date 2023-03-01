if [[ ! -x "`which poetry 2>/dev/null`" ]]
then
    read -p "You do not have poetry installed. Install now? (y/N)" choice
    case "$choice" in 
        y|Y ) python -m pip install poetry;;
        n|N|* ) echo "Aborted"; exit 1 ;;
    esac
fi
