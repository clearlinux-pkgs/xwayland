#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
# Source0 file verified with key 0x14706DBE1E4B4540 (fourdan@xfce.org)
#
Name     : xwayland
Version  : 23.2.0
Release  : 41
URL      : https://xorg.freedesktop.org/archive/individual/xserver/xwayland-23.2.0.tar.xz
Source0  : https://xorg.freedesktop.org/archive/individual/xserver/xwayland-23.2.0.tar.xz
Source1  : https://xorg.freedesktop.org/archive/individual/xserver/xwayland-23.2.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xwayland-bin = %{version}-%{release}
Requires: xwayland-data = %{version}-%{release}
Requires: xwayland-license = %{version}-%{release}
Requires: xwayland-man = %{version}-%{release}
Requires: xkbcomp
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : font-util-dev
BuildRequires : freetype-dev
BuildRequires : graphviz
BuildRequires : libdmx-dev
BuildRequires : libei-dev
BuildRequires : libgcrypt-dev
BuildRequires : libxshmfence-dev
BuildRequires : libxslt-bin
BuildRequires : nettle-dev
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libbsd)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(libxcvt)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xf86dgaproto)
BuildRequires : pkgconfig(xfont)
BuildRequires : pkgconfig(xfont2)
BuildRequires : pkgconfig(xkbcomp)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : wayland-dev
BuildRequires : wayland-protocols-dev
BuildRequires : xkbcomp-bin
BuildRequires : xmlto
BuildRequires : xtrans-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
X Server
--------
The X server accepts requests from client applications to create windows,
which are (normally rectangular) "virtual screens" that the client program
can draw into.

%package bin
Summary: bin components for the xwayland package.
Group: Binaries
Requires: xwayland-data = %{version}-%{release}
Requires: xwayland-license = %{version}-%{release}

%description bin
bin components for the xwayland package.


%package data
Summary: data components for the xwayland package.
Group: Data

%description data
data components for the xwayland package.


%package dev
Summary: dev components for the xwayland package.
Group: Development
Requires: xwayland-bin = %{version}-%{release}
Requires: xwayland-data = %{version}-%{release}
Provides: xwayland-devel = %{version}-%{release}
Requires: xwayland = %{version}-%{release}

%description dev
dev components for the xwayland package.


%package license
Summary: license components for the xwayland package.
Group: Default

%description license
license components for the xwayland package.


%package man
Summary: man components for the xwayland package.
Group: Default

%description man
man components for the xwayland package.


%prep
%setup -q -n xwayland-23.2.0
cd %{_builddir}/xwayland-23.2.0
pushd ..
cp -a xwayland-23.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692204339
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/xwayland
cp %{_builddir}/xwayland-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xwayland/11d1ae389a1a78f7832586e4c2a0c3c7263b7475 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
## Remove excluded files
rm -f %{buildroot}*/usr/share/man/man1/Xserver.1
rm -f %{buildroot}*/usr/lib64/xorg/protocol.txt
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/Xwayland
/usr/bin/Xwayland

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.freedesktop.Xwayland.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/xwayland.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xwayland/11d1ae389a1a78f7832586e4c2a0c3c7263b7475

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/Xwayland.1
