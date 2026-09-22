
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, List


@dataclass(frozen=True)
class Campaign:
    name: str
    channel: str
    daily_budget: float
    start_date: date
    end_date: Optional[date]
    target_audience: Dict[str, Any]
    creatives: List[Dict[str, str]]
    tracking: Dict[str, str]


class CampaignBuilder:
    def __init__(self):
      # TODO: 
      self._name = None
      self._channel = None
      self._daily_budget = None
      self._start_date = None
      self._end_date = None
      self._target_audience = {}
      self._creatives = []
      self._tracking = {}




    def with_name(self, name: str): #setters
      # TODO
      self._name = name
      return self


    def with_channel(self, channel: str):
      # TODO
      self._channel= channel
      return self

    def with_budget(self, daily_budget: float):
      # TODO
      self._daily_budget = daily_budget   
      return self

    def with_dates(self, start_date, end_date=None):
      # TODO
      self._start_date = start_date       
      self._end_date = end_date
      return self

    def with_audience(self, **kwargs):
      self._target_audience.update(kwargs)

      return self

    def add_creative(self, headline: str, image_url: str):
      self._creatives.append({"headline": headline, "image_url": image_url})
      return self

    def with_tracking(self, **kwargs):
      self._tracking.update(kwargs)
      return self

    def build(self) -> Campaign:
      # TODO: Validations and return Campaign instance
      if not self._name:
        raise ValueError("Campaign must have a name.")
      if not self._channel:
        raise ValueError("Campaign channel cannot be empty.")
      if not self._daily_budget or self._daily_budget <= 0:
        raise ValueError("Daily budget must exist and be a positive number.")
      if self._end_date is not None and self._end_date < self._start_date:
        raise ValueError("Start date must be before or equal to end date.")
      if not self._creatives:
        raise ValueError("At least one creative must be provided.")
      
      
      return Campaign(
          name=self._name,
          channel=self._channel,
          daily_budget=self._daily_budget,
          start_date=self._start_date,
          end_date=self._end_date,
          target_audience=self._target_audience,
          creatives=self._creatives,
          tracking=self._tracking,
      )
