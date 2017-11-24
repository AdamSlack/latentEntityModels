import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'

import { AppComponent } from './app.component';
import { BookExplorerComponent } from './book-explorer/book-explorer.component';
import { ExplorerApiService } from './services/explorer-api.service';

@NgModule({
  declarations: [
    AppComponent,
    BookExplorerComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [ExplorerApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
