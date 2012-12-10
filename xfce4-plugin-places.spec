%define		rname	xfce4-places-plugin

Summary:	Quick access to folders, documents, and removable media
Name:		xfce4-plugin-places
Version:	1.5.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-places-plugin/1.5/%{rname}-%{version}.tar.bz2
# Source0-md5:	84c39fb123e07e1c7caaf006d9383656
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
BuildRequires:	Thunar-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkg-config
BuildRequires:	xfce4-panel-devel
Requires:	gvfs
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Written by Diego Ongaro, this plugin is a menu with quick access to
folders, documents, and removable media. The places plugin brings much
of the functionality of GNOME's Places menu to Xfce.

The plugin puts a simple button on the panel. Clicking on this button
opens up a menu with the following:
1) System-defined directories (home folder, trash, desktop, file
   system)
2) Removable media (using thunar-vfs)
3) User-defined bookmarks (reads ~/.gtk-bookmarks)
4) Search program launcher (optional)
5) Recent documents submenu (requires GTK+ v2.10 or greater)

%prep
%setup -qn %{rname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{rname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{rname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xfce4-popup-places
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libplaces.so
%{_datadir}/xfce4/panel/plugins/places.desktop

