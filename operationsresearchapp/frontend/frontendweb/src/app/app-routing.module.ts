import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LinearProgrammingComponent } from './linearprogramming/linearprogramming.component';
import { MixedIntegerProgrammingComponent } from './mixed-integer-programming/mixed-integer-programming.component';

const routes: Routes = [
  {
    path: 'linearprogramming',
    component: LinearProgrammingComponent
  },
  {
    path: 'mixedintegerprogramming',
    component: MixedIntegerProgrammingComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
