%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kolourpaint
Summary:	kolourpaint
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9c8dfe1b5464dc3cc1a19d80c0c8330c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.7.0
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KolourPaint is a simple painting program to quickly create raster
images. It is useful as a touch-up tool and simple image editing
tasks.

Features: Support for drawing various shapes - lines, rectangles,
rounded rectangles, ovals and polygons.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolourpaint
%attr(755,root,root) %{_libdir}/libkolourpaint_lgpl.so
%attr(755,root,root) %{_libdir}/libkolourpaint_lgpl.so.5
%{_desktopdir}/org.kde.kolourpaint.desktop
%{_iconsdir}/hicolor/16x16/apps/kolourpaint.png
%{_iconsdir}/hicolor/22x22/apps/kolourpaint.png
%{_iconsdir}/hicolor/32x32/apps/kolourpaint.png
%{_iconsdir}/hicolor/48x48/apps/kolourpaint.png
%{_iconsdir}/hicolor/scalable/apps/kolourpaint.svgz
%{_datadir}/kolourpaint
%{_datadir}/kxmlgui5/kolourpaint
%{_datadir}/metainfo/org.kde.kolourpaint.appdata.xml
