const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
    try {
        console.log('Launching browser...');
        const browser = await puppeteer.launch({
            headless: "new"
        });
        const page = await browser.newPage();

        const filePath = path.join(__dirname, 'cv_print.html');
        console.log(`Opening file: ${filePath}`);

        await page.goto(`file://${filePath}`, {
            waitUntil: 'networkidle0'
        });

        console.log('Generating PDF...');
        await page.pdf({
            path: 'Emad_Alhamou_CV.pdf',
            format: 'A4',
            printBackground: true,
            margin: {
                top: '0',
                right: '0',
                bottom: '0',
                left: '0'
            }
        });

        await browser.close();
        console.log('Success! PDF saved as Emad_Alhamou_CV.pdf');
    } catch (error) {
        console.error('Error generating PDF:', error);
        console.log('\nTo run this script, you need to install puppeteer:\nnpm install puppeteer');
    }
})();
