# https://github.com/grpc-ecosystem/grpc-gateway
%global goipath         github.com/grpc-ecosystem/grpc-gateway
%global commit          8cc3a55af3bcf171a1c23a90c4df9cf591706104

%gometa -i

Name:           golang-github-grpc-ecosystem-grpc-gateway
Version:        1.0.0
Release:        0.12%{?dist}
Summary:        GRPC to JSON proxy generator
# Detected licences
# - BSD (3 clause) at 'LICENSE.txt'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/golang/glog)
BuildRequires: golang(github.com/golang/protobuf/jsonpb)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/descriptor)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/generator)
BuildRequires: golang(github.com/golang/protobuf/protoc-gen-go/plugin)
BuildRequires: golang(github.com/golang/protobuf/ptypes/empty)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/genproto/googleapis/api/annotations)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/grpclog)
BuildRequires: golang(google.golang.org/grpc/metadata)
# test dependencies
BuildRequires: golang(github.com/golang/protobuf/ptypes/duration)
BuildRequires: golang(github.com/golang/protobuf/ptypes/struct)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/golang/protobuf/ptypes/wrappers)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml runtime/internal/stream_chunk.proto examples

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.11.git8cc3a55
- Upload glide files

* Thu Mar 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.10.git8cc3a55
- Bump to 8cc3a55af3bcf171a1c23a90c4df9cf591706104
  related: #1405682

* Tue Feb 20 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.9.git18d1596
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.git18d1596
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.7.git18d1596
- Bump to upstream 18d159699f2e83fc5bb9ef2f79465ca3f3122676
  related: #1405682

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.git84398b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.git84398b9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.4.git84398b9
- Bump to upstream 84398b94e188ee336f307779b57b3aa91af7063c
  related: #1405682

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.gitf52d055
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-0.2.gitf52d055
- Polish the spec file
  resolves: #1405682

* Tue Aug 02 2016 jchaloup <jchaloup@redhat.com> - 1.0.0-0.1.gitf52d055
- First package for Fedora
  resolves: #1362419
