import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'

import { AppComponent } from './app.component';
import { BookExplorerComponent } from './book-explorer/book-explorer.component';
import { ExplorerApiService } from './services/explorer-api.service';
import { BannerComponent } from './banner/banner.component';
import { BannegstrComponent } from './bannegstr/bannegstr.component';
import { TopicModelsComponent } from './topic-models/topic-models.component';

@NgModule({
  declarations: [
    AppComponent,
    BookExplorerComponent,
    BannerComponent,
    BannegstrComponent,
    TopicModelsComponent
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
