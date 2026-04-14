%global debug_package %{nil}

Name:		newsraft
Version:	0.36
Release:	1
Source0:	https://codeberg.org/newsraft/newsraft/archive/%{name}-%{version}.tar.gz
Summary:	Feed reader with text-based user interface
URL:		https://codeberg.org/newsraft/newsraft
License:	ISC
Group:		Reader

BuildRequires:  make
BuildRequires:  gperf
BuildRequires:  scdoc
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(expat)

Requires:   curl
Requires:   expat
Requires:   %{_lib}sqlite3_0
Requires:   %{_lib}gumbo

%description
Newsraft is a small text based program for reading syndication feeds.
It obtains content from a given set of sources and lets you browse
it all via one streamlined user interface.

%prep
%autosetup -p1 -n %{name}
mv doc/license*.txt %{_builddir}/%{name}

%build
%make_build

%install
%make_install

%files
%doc README.md
%license license*.txt
/usr/local/bin/newsraft
/usr/local/share/icons/hicolor/scalable/apps/newsraft.svg
/usr/local/share/man/man1/newsraft.1
/usr/local/share/newsraft/examples/config
/usr/local/share/newsraft/examples/feeds
