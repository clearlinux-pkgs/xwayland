#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x14706DBE1E4B4540 (fourdan@xfce.org)
#
Name     : xwayland
Version  : 22.1.3
Release  : 19
URL      : https://xorg.freedesktop.org/archive/individual/xserver/xwayland-22.1.3.tar.xz
Source0  : https://xorg.freedesktop.org/archive/individual/xserver/xwayland-22.1.3.tar.xz
Source1  : https://xorg.freedesktop.org/archive/individual/xserver/xwayland-22.1.3.tar.xz.sig
Summary  : X Server for Wayland
Group    : Development/Tools
License  : MIT
Requires: xwayland-bin = %{version}-%{release}
Requires: xwayland-filemap = %{version}-%{release}
Requires: xwayland-license = %{version}-%{release}
Requires: xwayland-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : font-util-dev
BuildRequires : freetype-dev
BuildRequires : graphviz
BuildRequires : libdmx-dev
BuildRequires : libgcrypt-dev
BuildRequires : libxshmfence-dev
BuildRequires : libxslt-bin
BuildRequires : nettle-dev
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libbsd)
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
Requires: xwayland-license = %{version}-%{release}
Requires: xwayland-filemap = %{version}-%{release}

%description bin
bin components for the xwayland package.


%package dev
Summary: dev components for the xwayland package.
Group: Development
Requires: xwayland-bin = %{version}-%{release}
Provides: xwayland-devel = %{version}-%{release}
Requires: xwayland = %{version}-%{release}

%description dev
dev components for the xwayland package.


%package filemap
Summary: filemap components for the xwayland package.
Group: Default

%description filemap
filemap components for the xwayland package.


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
%setup -q -n xwayland-22.1.3
cd %{_builddir}/xwayland-22.1.3
pushd ..
cp -a xwayland-22.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657645129
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/xwayland
cp %{_builddir}/xwayland-22.1.3/COPYING %{buildroot}/usr/share/package-licenses/xwayland/11d1ae389a1a78f7832586e4c2a0c3c7263b7475
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
/usr/bin/Xwayland
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/xwayland.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-xwayland

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xwayland/11d1ae389a1a78f7832586e4c2a0c3c7263b7475

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/Xwayland.1
