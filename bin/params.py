'''Parameter dataclasses.'''

from dataclasses import dataclass, field
from datetime import date, datetime
import json
from pathlib import Path
from typing import List


DATE_FORMAT = '%Y-%m-%d'
DEFAULT_START_DATE = datetime.strptime('2023-11-01', DATE_FORMAT)
DEFAULT_END_DATE = datetime.strptime('2023-11-10', DATE_FORMAT)


@dataclass
class AssayParams:
    '''Parameters for assay data generation.'''

    seed: int = None
    startdate: date = None
    enddate: date = None
    experiments: dict
    filename_length: int = 8
    locale: str = 'en_IN'
    staff: int = 1
    experiments: int = 1
    invalid: float = 0.1
    control: float = 5.0
    treated: float = 8.0
    stdev: float = 3.0
    treatment: str = None
    controls: List[str] = field(default_factory=list)

    def __post_init__(self):
        '''Convert dates if provided.'''
        if self.startdate is None:
            self.startdate = DEFAULT_START_DATE
        else:
            self.startdate = datetime.strptime(self.startdate, DATE_FORMAT)

        if self.enddate is None:
            self.enddate = DEFAULT_END_DATE
        else:
            self.enddate = datetime.strptime(self.enddate, DATE_FORMAT)


@dataclass
class GenomeParams:
    '''Gene sequence parameters.'''
    length: int = None
    num_genomes: int = None
    num_snp: int = None
    prob_other: float = None
    seed: int = None


@dataclass
class SampleParams:
    '''Sampled snail parameters.'''
    mutant: float = None
    normal: float = None
    seed: int = None


def load_params(cls, filename):
    '''Load parameters from file.'''
    return cls(**json.loads(Path(filename).read_text()))
