%global commit      519185a45f0c39e4e66261c47e74768107f334eb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190628

Name:           vpnswitcher
Version:        0
Release:        1.%{date}git%{shortcommit}%{?dist}

License:        MIT
Summary:        Desktop application for controlling Wireguard

URL:            https://github.com/xshram/vpnswitcher
Source0:        %{url}/tarball/%{commit}#/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  gtk3-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject

%description
GUI Application for controlling your vpn(Wireguard)

%prep
%autosetup -n xshram-%{name}-%{shortcommit}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

