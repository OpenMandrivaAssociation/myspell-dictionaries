#!/bin/bash

PLANG=$1
CONTENTS=$2
PNAME=$3
LICENSE=$4
RENAMED_FROM="$5"

##
## Common section
##

function GeneratePackageFilelist() {
dict=
hyph=
thes=
EXTRA=
if [ -z "${CONTENTS/*DICT*}" ]; then
    dict="%doc doc/DICT/$PLANG/*"
fi
if [ -z "${CONTENTS/*HYPH*}" ]; then
    hyph="%doc doc/HYPH/hyph_$PLANG/*"
fi
if [ -z "${CONTENTS/*THES*}" ]; then
    thes="%doc doc/THES/th_$PLANG/*"
fi
EXTRA=" -f $PLANG.files"
cat << EOF

%files -n $PACKAGE$EXTRA
%defattr(-,root,root)
$dict
$hyph
$thes
EOF
}

function GeneratePackageScripts() {
echo "%post -n $PACKAGE"
for ptype in $CONTENTS; do
    if [ $ptype == "DICT" ]; then
	FILE="$PLANG"
    else
	FILE="$(echo ${ptype/THES/th} | tr [A-Z] [a-z])_$PLANG"
    fi

    for country in $ISOCOUNTRY; do
	cat << EOF
if [[ ! -f "%{dictdir}/dictionary.lst" ]] || \
      ! grep -q "^$ptype[ \t]*$ISOCODE[ \t]*$country[ \t]*$FILE" %{dictdir}/dictionary.lst
then
  echo "$ptype $ISOCODE $country $FILE" >> %{dictdir}/dictionary.lst
fi
EOF
    done
done

echo
echo "%preun -n $PACKAGE"
for ptype in $CONTENTS; do
    if [ $ptype == "DICT" ]; then
	FILE="$PLANG"
    else
	FILE="$(echo ${ptype/THES/th} | tr [A-Z] [a-z])_$PLANG"
    fi

    for country in $ISOCOUNTRY; do
	cat << EOF
if [[ "\$1" = "0" ]]; then
  perl -ni -e "/^$ptype\s*$ISOCODE\s*$country\s*$FILE\$/ or print" %{dictdir}/dictionary.lst
fi
EOF
    done
done
}

##
## Handle PackageInfo
##

function GeneratePackageInfo() {
dict=
hyph=
thes=
if [ -z "${CONTENTS/*DICT*}" ]; then
    dict="
Provides:	myspell-dictionary = %{version}-%{release}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 2
"
fi
if [ -z "${CONTENTS/*HYPH*}" ]; then
    unset hyph
    if [ -n "$LOCALECODE" ]; then
        hyph="
Obsoletes:	myspell-hyph-$LOCALECODE < %{version}-%{release}
Provides:	myspell-hyph-$LOCALECODE = %{version}-%{release}"
    fi
    hyph="$hyph
Obsoletes:	myspell-hyph-$PLANG < %{version}-%{release}
Provides:	myspell-hyph-$PLANG = %{version}-%{release}
Provides:	myspell-hyphenation = %{version}-%{release}
"
fi
if [ -z "${CONTENTS/*THES*}" ]; then
    unset thes
    if [ -n "$LOCALECODE" ]; then
        thes="
Obsoletes:	myspell-thes-$LOCALECODE < %{version}-%{release}
Provides:	myspell-thes-$LOCALECODE = %{version}-%{release}"
    fi
    thes="$thes
Obsoletes:	myspell-thes-$PLANG < %{version}-%{release}
Provides:	myspell-thes-$PLANG = %{version}-%{release}
Provides:	myspell-thesaurus = %{version}-%{release}
"
fi
cat << EOF
%package -n $PACKAGE
Summary:	$SHORT_LANGNAME dictionaries
License:	$LICENSE
Group:		System/Internationalization
EOF
[ -z "$LOCALECODE" ] || cat << EOF
Provides:	myspell-$LOCALECODE = %{version}-%{release}
EOF
for i in $RENAMED_FROM; do
	echo "%rename myspell-$i"
done
cat << EOF
$dict
$hyph
$thes
EOF
[ -z "$LOCALECODE" ] || cat << EOF
Requires:	locales-$LOCALECODE
EOF
cat << EOF

%description -n $PACKAGE
$PACKAGE contains spell checking data in 
$SHORT_LANGNAME to be used by 
OpenOffice.org or MySpell-capable applications like Mozilla.
With this extension, you can compose a document in
$SHORT_LANGNAME and check for the typos easily.

EOF
}

##
## Main
##

[[ -z "$COMMAND$PLANG$PNAME$LICENSE" ]] && {
  echo "%{error: ${0##*/}: Bad arguments}"
  exit 0
}

ISOCODE=${PLANG%%_*} ISOCOUNTRY=${PLANG#*_}
[[ "$ISOCODE" = "$ISOCOUNTRY" ]] && ISOCOUNTRY=""

case $ISOCODE:$ISOCOUNTRY in
cop:EG|fj:FJ|la:LA|ny:MW|qu:BO|tet:ID|an:ES|gug*|kmr*)
  LOCALECODE=
  ;;
csb:CSB)
  LOCALECODE=pl
  ;;
gsc:FR)
  LOCALECODE=oc
  ;;
nb:NO|nn:NO)
  LOCALECODE=no
  ;;
ns:ZA)
  LOCALECODE=nso
  ;;
*)
  LOCALECODE=$ISOCODE
  ;;
esac

PACKAGE="myspell-$PLANG"

SHORT_LANGNAME=`echo "$PNAME" | sed -e "s/\([A-Z][^ ]*\).*/\1/"`
GeneratePackageInfo

#ISOCOUNTRY="$PLANG"
GeneratePackageScripts

GeneratePackageFilelist

exit 0
