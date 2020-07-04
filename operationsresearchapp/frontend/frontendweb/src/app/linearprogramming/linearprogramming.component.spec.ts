import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LinearProgrammingComponent } from './linearprogramming.component';

describe('LinearprogrammingComponent', () => {
  let component: LinearProgrammingComponent;
  let fixture: ComponentFixture<LinearProgrammingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LinearProgrammingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LinearProgrammingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
