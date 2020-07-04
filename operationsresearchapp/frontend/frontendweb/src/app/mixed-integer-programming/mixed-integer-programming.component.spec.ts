import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MixedIntegerProgrammingComponent } from './mixed-integer-programming.component';

describe('MixedIntegerProgrammingComponent', () => {
  let component: MixedIntegerProgrammingComponent;
  let fixture: ComponentFixture<MixedIntegerProgrammingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MixedIntegerProgrammingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MixedIntegerProgrammingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
