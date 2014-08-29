from artemis.test_mechanism import ArtemisTestFixture, dataset


@dataset(["corr-01"])
class TestCorr01(ArtemisTestFixture):
    """
    Le test test_corr_01_01 ne renvoie pas d'itinéraire car le nombre de correspondance est > 10
    """

    def test_corr_01_01(self):
        self.journey(_from="stop_area:CR1:SA:1",
                     to="stop_area:CR1:SA:13", datetime="20041210T0700")

    def test_corr_01_02(self):
        self.journey(_from="stop_area:CR1:SA:1",
                     to="stop_area:CR1:SA:13", datetime="20041210T0700", max_nb_transfers=12)
