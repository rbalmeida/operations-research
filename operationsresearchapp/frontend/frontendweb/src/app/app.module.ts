import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LinearProgrammingComponent } from './linearprogramming/linearprogramming.component';
import { MixedIntegerProgrammingComponent } from './mixed-integer-programming/mixed-integer-programming.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module'
import { FlexLayoutModule } from '@angular/flex-layout'
import { MainNavigationComponent} from './main-navigation/main-navigation.component'


@NgModule({
  declarations: [
    AppComponent,
    LinearProgrammingComponent,
    MixedIntegerProgrammingComponent,
    MainNavigationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
