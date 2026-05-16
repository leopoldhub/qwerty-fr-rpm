# requires rpm-build package installed
RPMBUILD=rpmbuild
RM=rm -rf

SPEC=xkb-qwerty-fr.spec
TOPDIR:=$(CURDIR)
RPMFILENAME=%{NAME}_%{VERSION}_linux.%{ARCH}.rpm

RPMDIR=$(TOPDIR)/RPMS
BUILDDIR=$(TOPDIR)/BUILD
BUILDROOTDIR=$(TOPDIR)/BUILDROOT
SRCRPMDIR=$(TOPDIR)/SRPMS

.PHONY: rpm
rpm:
	$(RPMBUILD) -bb $(SPEC) \
		--define "_sourcedir $(TOPDIR)/../.." \
		--define "_rpmfilename $(RPMFILENAME)" \
		--define "_rpmdir $(RPMDIR)" \
		--define "_builddir $(BUILDDIR)" \
		--define "_buildrootdir $(BUILDROOTDIR)" \
		--define "_srcrpmdir $(SRCRPMDIR)"

rpm_src:
	$(RPMBUILD) -bs $(SPEC) \
		--define "_sourcedir $(TOPDIR)/../.." \
		--define "_srcrpmdir $(SRCRPMDIR)"

.PHONY: clean
clean:
	$(RM) $(RPMDIR) $(BUILDDIR) $(BUILDROOTDIR) $(SRCRPMDIR)
