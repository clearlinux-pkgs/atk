#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : atk
Version  : 2.30.0
Release  : 24
URL      : https://download.gnome.org/sources/atk/2.30/atk-2.30.0.tar.xz
Source0  : https://download.gnome.org/sources/atk/2.30/atk-2.30.0.tar.xz
Summary  : Accessibility Toolkit
Group    : Development/Tools
License  : LGPL-2.0
Requires: atk-data
Requires: atk-lib
Requires: atk-license
Requires: atk-locales
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev

%description
ATK - The Accessibility Toolkit
===============================
For more information about ATK and accessibility in GNOME, see:

%package data
Summary: data components for the atk package.
Group: Data

%description data
data components for the atk package.


%package dev
Summary: dev components for the atk package.
Group: Development
Requires: atk-lib
Requires: atk-data
Provides: atk-devel

%description dev
dev components for the atk package.


%package dev32
Summary: dev32 components for the atk package.
Group: Default
Requires: atk-lib32
Requires: atk-data
Requires: atk-dev

%description dev32
dev32 components for the atk package.


%package lib
Summary: lib components for the atk package.
Group: Libraries
Requires: atk-data
Requires: atk-license

%description lib
lib components for the atk package.


%package lib32
Summary: lib32 components for the atk package.
Group: Default
Requires: atk-data
Requires: atk-license

%description lib32
lib32 components for the atk package.


%package license
Summary: license components for the atk package.
Group: Default

%description license
license components for the atk package.


%package locales
Summary: locales components for the atk package.
Group: Default

%description locales
locales components for the atk package.


%prep
%setup -q -n atk-2.30.0
pushd ..
cp -a atk-2.30.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536500163
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
CFLAGS="$CFLAGS -m32" CXXFLAGS="$CXXFLAGS -m32" LDFLAGS="$LDFLAGS -m32" PKG_CONFIG_PATH="/usr/lib32/pkgconfig" meson --libdir=/usr/lib32 --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/doc/atk
cp COPYING %{buildroot}/usr/share/doc/atk/COPYING
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang atk10

%files
%defattr(-,root,root,-)
/usr/lib32/girepository-1.0/Atk-1.0.typelib

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Atk-1.0.typelib
/usr/share/gir-1.0/*.gir

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
/usr/lib64/libatk-1.0.so
/usr/lib64/pkgconfig/atk.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libatk-1.0.so
/usr/lib32/pkgconfig/32atk.pc
/usr/lib32/pkgconfig/atk.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libatk-1.0.so.0
/usr/lib64/libatk-1.0.so.0.23009.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libatk-1.0.so.0
/usr/lib32/libatk-1.0.so.0.23009.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/atk/COPYING

%files locales -f atk10.lang
%defattr(-,root,root,-)

