# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-kat

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    The unofficial client for vk.com
Version:    0.5.4
Release:    42
Group:      Qt/Qt
License:    GNU GPLv3
URL:        https://vk.com/mobilevika
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-kat.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
The unofficial client for the most popular social network developed by Linux User Group Udmurtia and shared under the terms of the GNU General Public Licence version 3.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/
cp %{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/108x108/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
cp %{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/172x172/apps/
cp %{buildroot}/%{_datadir}/icons/hicolor/86x86/apps/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/172x172/apps/

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
