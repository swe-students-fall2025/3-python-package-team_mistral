import pytest
from conversations.banter import banter


class TestBanter:

    # Basic functionality tests
    def test_returns_string(self):
        """Verify banter returns a non-empty string."""
        for intensity in ["mild", "medium", "intense"]:
            result = banter(intensity)
            assert isinstance(result, str), f"Expected string, got {type(result)}"
            assert len(result) > 0, "Expected non-empty string"

    def test_multiple_calls_vary(self):
        """Verify banter returns different results across multiple calls."""
        results = [banter("mild") for _ in range(20)]
        assert len(set(results)) >= 2, "Expected variation in output"

    def test_output_is_lowercase(self):
        """Verify insults start with lowercase letter."""
        result = banter("medium")
        assert result[0].islower(), "Expected insult to start with lowercase"

    # Name parameter tests
    def test_name_appears_in_output(self):
        """Check that provided name appears in the result."""
        name = "Alice"
        result = banter("mild", name)
        assert name in result, f"Expected '{name}' in output"

    def test_name_at_start_with_comma(self):
        """Verify name formatting starts with 'Name,'."""
        name = "Bob"
        result = banter("intense", name)
        assert result.startswith(f"{name},"), f"Expected '{name},' at start"

    def test_no_name_no_comma(self):
        """Verify output without name doesn't start with comma."""
        result = banter("medium")
        assert not result.startswith(","), "Shouldn't start with comma"

    # Intensity level tests
    def test_mild_intensity_works(self):
        mild_keywords = ["penny", "drizzle", "software", "secret", "loading"]
        found = False
        for _ in range(30):
            if any(word in banter("mild").lower() for word in mild_keywords):
                found = True
                break
        assert found, "Expected mild-specific content"

    def test_medium_intensity_works(self):
        """Test medium intensity returns appropriate content."""
        medium_keywords = ["envy", "far someday", "left hand", "participation", "exit"]
        found = False
        for _ in range(30):
            if any(word in banter("medium").lower() for word in medium_keywords):
                found = True
                break
        assert found, "Expected medium-specific content"

    def test_intense_intensity_works(self):
        """Test intense intensity returns corresponding content."""
        intense_keywords = ["cloud", "bad luck", "lost", "tree", "monday", "before picture"]
        found = False
        for _ in range(30):
            if any(word in banter("intense").lower() for word in intense_keywords):
                found = True
                break
        assert found, "Expected intense-specific content"

    # Error handling tests
    def test_invalid_intensity_raises_error(self):
        with pytest.raises(KeyError):
            banter("extreme")

    def test_empty_intensity_raises_error(self):
        with pytest.raises(KeyError):
            banter("")

    def test_wrong_type_intensity_raises_error(self):
        with pytest.raises(KeyError):
            banter(123)