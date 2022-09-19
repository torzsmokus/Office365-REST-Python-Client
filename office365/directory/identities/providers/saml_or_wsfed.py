from office365.directory.identities.providers.base import IdentityProviderBase


class SamlOrWsFedProvider(IdentityProviderBase):
    """An abstract type that provides configuration details for setting up a SAML or WS-Fed external domain-based
    identity provider (IdP)."""

    @property
    def issuer_uri(self):
        """
        Issuer URI of the federation server.

        :rtype: str
        """
        return self.properties.get("issuerUri", None)
