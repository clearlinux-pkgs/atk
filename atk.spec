#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : atk
Version  : 2.22.0
Release  : 10
URL      : http://ftp.acc.umu.se/pub/gnome/sources/atk/2.22/atk-2.22.0.tar.xz
Source0  : http://ftp.acc.umu.se/pub/gnome/sources/atk/2.22/atk-2.22.0.tar.xz
Summary  : Accessibility Toolkit, Not Installed
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: atk-lib
Requires: atk-doc
Requires: atk-locales
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(glib-2.0)

%description
Handy library of accessibility functions. Development libs and headers
are in atk-devel.

%package dev
Summary: dev components for the atk package.
Group: Development
Requires: atk-lib
Provides: atk-devel

%description dev
dev components for the atk package.


%package dev32
Summary: dev32 components for the atk package.
Group: Default
Requires: atk-lib32
Requires: atk-dev

%description dev32
dev32 components for the atk package.


%package doc
Summary: doc components for the atk package.
Group: Documentation

%description doc
doc components for the atk package.


%package lib
Summary: lib components for the atk package.
Group: Libraries

%description lib
lib components for the atk package.


%package lib32
Summary: lib32 components for the atk package.
Group: Default

%description lib32
lib32 components for the atk package.


%package locales
Summary: locales components for the atk package.
Group: Default

%description locales
locales components for the atk package.


%prep
%setup -q -n atk-2.22.0
pushd ..
cp -a atk-2.22.0 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32 "
export CXXFLAGS="$CXXFLAGS -m32 "
export LDFLAGS="$LDFLAGS -m32 "
%configure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang atk10

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/Atk-1.0.typelib

%files dev
%defattr(-,root,root,-)
/usr/include/atk-1.0/atk/atk-enum-types.h
/usr/include/atk-1.0/atk/atk.h
/usr/include/atk-1.0/atk/atkaction.h
/usr/include/atk-1.0/atk/atkcomponent.h
/usr/include/atk-1.0/atk/atkdocument.h
/usr/include/atk-1.0/atk/atkeditabletext.h
/usr/include/atk-1.0/atk/atkgobjectaccessible.h
/usr/include/atk-1.0/atk/atkhyperlink.h
/usr/include/atk-1.0/atk/atkhyperlinkimpl.h
/usr/include/atk-1.0/atk/atkhypertext.h
/usr/include/atk-1.0/atk/atkimage.h
/usr/include/atk-1.0/atk/atkmisc.h
/usr/include/atk-1.0/atk/atknoopobject.h
/usr/include/atk-1.0/atk/atknoopobjectfactory.h
/usr/include/atk-1.0/atk/atkobject.h
/usr/include/atk-1.0/atk/atkobjectfactory.h
/usr/include/atk-1.0/atk/atkplug.h
/usr/include/atk-1.0/atk/atkrange.h
/usr/include/atk-1.0/atk/atkregistry.h
/usr/include/atk-1.0/atk/atkrelation.h
/usr/include/atk-1.0/atk/atkrelationset.h
/usr/include/atk-1.0/atk/atkrelationtype.h
/usr/include/atk-1.0/atk/atkselection.h
/usr/include/atk-1.0/atk/atksocket.h
/usr/include/atk-1.0/atk/atkstate.h
/usr/include/atk-1.0/atk/atkstateset.h
/usr/include/atk-1.0/atk/atkstreamablecontent.h
/usr/include/atk-1.0/atk/atktable.h
/usr/include/atk-1.0/atk/atktablecell.h
/usr/include/atk-1.0/atk/atktext.h
/usr/include/atk-1.0/atk/atkutil.h
/usr/include/atk-1.0/atk/atkvalue.h
/usr/include/atk-1.0/atk/atkversion.h
/usr/include/atk-1.0/atk/atkwindow.h
/usr/lib64/girepository-1.0/Atk-1.0.typelib
/usr/lib64/libatk-1.0.so
/usr/lib64/pkgconfig/atk.pc
/usr/share/gir-1.0/*.gir

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libatk-1.0.so
/usr/lib32/pkgconfig/32atk.pc
/usr/lib32/pkgconfig/atk.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/atk/AtkAction.html
/usr/share/gtk-doc/html/atk/AtkComponent.html
/usr/share/gtk-doc/html/atk/AtkDocument.html
/usr/share/gtk-doc/html/atk/AtkEditableText.html
/usr/share/gtk-doc/html/atk/AtkGObjectAccessible.html
/usr/share/gtk-doc/html/atk/AtkHyperlink.html
/usr/share/gtk-doc/html/atk/AtkHypertext.html
/usr/share/gtk-doc/html/atk/AtkImage.html
/usr/share/gtk-doc/html/atk/AtkMisc.html
/usr/share/gtk-doc/html/atk/AtkNoOpObject.html
/usr/share/gtk-doc/html/atk/AtkNoOpObjectFactory.html
/usr/share/gtk-doc/html/atk/AtkObject.html
/usr/share/gtk-doc/html/atk/AtkObjectFactory.html
/usr/share/gtk-doc/html/atk/AtkRegistry.html
/usr/share/gtk-doc/html/atk/AtkRelation.html
/usr/share/gtk-doc/html/atk/AtkRelationSet.html
/usr/share/gtk-doc/html/atk/AtkSelection.html
/usr/share/gtk-doc/html/atk/AtkStateSet.html
/usr/share/gtk-doc/html/atk/AtkStreamableContent.html
/usr/share/gtk-doc/html/atk/AtkTable.html
/usr/share/gtk-doc/html/atk/AtkTableCell.html
/usr/share/gtk-doc/html/atk/AtkText.html
/usr/share/gtk-doc/html/atk/AtkUtil.html
/usr/share/gtk-doc/html/atk/AtkValue.html
/usr/share/gtk-doc/html/atk/AtkWindow.html
/usr/share/gtk-doc/html/atk/accessibles.html
/usr/share/gtk-doc/html/atk/api-index-1-12.html
/usr/share/gtk-doc/html/atk/api-index-1-13.html
/usr/share/gtk-doc/html/atk/api-index-1-20.html
/usr/share/gtk-doc/html/atk/api-index-1-22.html
/usr/share/gtk-doc/html/atk/api-index-1-3.html
/usr/share/gtk-doc/html/atk/api-index-1-30.html
/usr/share/gtk-doc/html/atk/api-index-1-4.html
/usr/share/gtk-doc/html/atk/api-index-1-6.html
/usr/share/gtk-doc/html/atk/api-index-1-9.html
/usr/share/gtk-doc/html/atk/api-index-2-10.html
/usr/share/gtk-doc/html/atk/api-index-2-12.html
/usr/share/gtk-doc/html/atk/api-index-2-2.html
/usr/share/gtk-doc/html/atk/api-index-2-8.html
/usr/share/gtk-doc/html/atk/api-index-deprecated.html
/usr/share/gtk-doc/html/atk/api-index-full.html
/usr/share/gtk-doc/html/atk/atk-AtkHyperlinkImpl.html
/usr/share/gtk-doc/html/atk/atk-AtkPlug.html
/usr/share/gtk-doc/html/atk/atk-AtkRange.html
/usr/share/gtk-doc/html/atk/atk-AtkSocket.html
/usr/share/gtk-doc/html/atk/atk-AtkState.html
/usr/share/gtk-doc/html/atk/atk-Versioning-Utilities.html
/usr/share/gtk-doc/html/atk/atk.devhelp2
/usr/share/gtk-doc/html/atk/atkobject.html
/usr/share/gtk-doc/html/atk/data.html
/usr/share/gtk-doc/html/atk/deprecated.html
/usr/share/gtk-doc/html/atk/home.png
/usr/share/gtk-doc/html/atk/index.html
/usr/share/gtk-doc/html/atk/interfaces.html
/usr/share/gtk-doc/html/atk/left-insensitive.png
/usr/share/gtk-doc/html/atk/left.png
/usr/share/gtk-doc/html/atk/overview.html
/usr/share/gtk-doc/html/atk/right-insensitive.png
/usr/share/gtk-doc/html/atk/right.png
/usr/share/gtk-doc/html/atk/style.css
/usr/share/gtk-doc/html/atk/toolkit.html
/usr/share/gtk-doc/html/atk/up-insensitive.png
/usr/share/gtk-doc/html/atk/up.png
/usr/share/gtk-doc/html/atk/utilities.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libatk-1.0.so.0
/usr/lib64/libatk-1.0.so.0.22209.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libatk-1.0.so.0
/usr/lib32/libatk-1.0.so.0.22209.1

%files locales -f atk10.lang 
%defattr(-,root,root,-)

