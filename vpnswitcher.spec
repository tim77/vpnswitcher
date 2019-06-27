


Name: vpnswitcher
Version: 1.0
Release: 1%{?dist}

License: MIT
Summary: Desktop application for controlling Wireguard

URL: https://github.com/xshram/vpnswitcher
Source0: https://github.com/xshram/vpnswitcher
BuildArch: noarch

BuildRequires: python3-gobject 
BuildRequires: python3-devel
BuildRequires: gtk3 
BuildRequires: python3-cairo-devel

%description
GUI Application for controlling your vpn(Wireguard)

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test
